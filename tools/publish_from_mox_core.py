"""Pubblica in modo deterministico i cataloghi canonici di mox-core."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
META = ROOT / "meta"
INDEX = ROOT / "indice.json"
MANIFEST = ROOT / "manifest.json"
SOURCE_REPOSITORY = "https://github.com/Dennis96/mox-core"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def build(source_dir: Path, source_repository: str, source_commit: str,
          generated_at: str) -> dict[Path, bytes]:
    if not re.fullmatch(r"[0-9a-f]{40}", source_commit):
        raise SystemExit("--source-commit deve essere uno SHA Git completo di 40 caratteri")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", generated_at):
        raise SystemExit("--generated-at deve usare UTC nel formato YYYY-MM-DDTHH:MM:SSZ")

    source_files = sorted(source_dir.glob("*.json"), key=lambda path: path.name)
    if not source_files:
        raise SystemExit(f"Nessun catalogo JSON in {source_dir}")

    outputs: dict[Path, bytes] = {}
    index_rows = []
    artifacts = {}
    for source in source_files:
        raw = source.read_bytes()
        try:
            payload = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise SystemExit(f"Catalogo non valido {source.name}: {exc}") from exc
        decks = payload.get("mazzi")
        if not isinstance(decks, list):
            raise SystemExit(f"Catalogo senza mazzi[]: {source.name}")

        relative = Path("meta") / source.name
        outputs[ROOT / relative] = raw
        digest = sha256(raw)
        artifacts[relative.as_posix()] = {"bytes": len(raw), "sha256": digest}
        index_rows.append({
            "nome": source.name,
            "formato": payload.get("formato"),
            "aggiornato": payload.get("aggiornato"),
            "mazzi": len(decks),
            "byte": len(raw),
            "sha256": digest,
        })

    index = {
        "versione": 1,
        "generato": generated_at[:10],
        "file": index_rows,
    }
    index_raw = json_bytes(index)
    outputs[INDEX] = index_raw
    artifacts["indice.json"] = {"bytes": len(index_raw), "sha256": sha256(index_raw)}

    manifest = {
        "versione": 1,
        "generated_only": True,
        "source_repository": source_repository,
        "source_commit": source_commit,
        "generated_at": generated_at,
        "artifacts": artifacts,
    }
    outputs[MANIFEST] = json_bytes(manifest)
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--source-repository", default=SOURCE_REPOSITORY)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--generated-at", required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    outputs = build(
        args.source_dir.resolve(), args.source_repository,
        args.source_commit.lower(), args.generated_at,
    )
    mismatches = []
    for target, expected in outputs.items():
        if args.check:
            if not target.is_file() or target.read_bytes() != expected:
                mismatches.append(str(target.relative_to(ROOT)))
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(expected)

    if mismatches:
        print("mox-meta non coincide con l'output atteso:", file=sys.stderr)
        for name in mismatches:
            print(f"- {name}", file=sys.stderr)
        return 1

    action = "verifica" if args.check else "pubblicazione"
    print(f"{action}: OK ({len(outputs) - 2} cataloghi + indice + manifest)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
