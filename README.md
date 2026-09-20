# mox-meta — le liste dei mazzi di Mox

Questo repository e' un **artefatto generated-only**. Contiene le liste dei mazzi che
[Mox](https://github.com/Dennis96) usa per il consigliere, il manifest di
provenienza e il solo strumento di pubblicazione. Non contiene il client ne'
dati personali.

La sola fonte modificabile e' `Dennis96/mox-core`, cartella `meta/`. Non aprire
PR che editano manualmente `meta/*.json` o `indice.json`: usare
`tools/publish_from_mox_core.py` dopo la validazione nel repository sorgente.
`manifest.json` registra commit sorgente, istante di generazione e hash degli
artefatti senza cambiare lo schema dei JSON consumati dai client.

Serve a una cosa sola: **le liste invecchiano e il programma no**. Quando esce
un set o arrivano delle carte bandite, Mox scarica da qui i file aggiornati
invece di far reinstallare tutto il pacchetto da 54 MB.

## Come lo usa Mox

All'avvio del consigliere, non piu' di una volta al giorno e sempre in
sottofondo: se la rete non c'e', si usano le liste del pacchetto e la finestra
si apre lo stesso. Un file scaricato **non viene creduto piu' di uno del
pacchetto**: la legalita' di ogni carta viene ricontrollata sul computer di chi
riceve il file, contro i set dichiarati dal suo client di MTG Arena.

A questo deposito non arriva nessuna informazione: sono file statici, e come
per qualsiasi sito l'unica cosa che si vede e' l'indirizzo IP di chi scarica.

## Cosa c'e' dentro

- `indice.json` — l'elenco dei file con data, numero di mazzi e impronta
  SHA-256, per non scaricare quello che non e' cambiato;
- `meta/*.json` — un file per formato: Standard, Alchemy, Pioneer, Historic,
  Timeless, Brawl e Historic Brawl.
- `manifest.json` — provenienza generated-only e hash di tutti gli artefatti;
- `tools/publish_from_mox_core.py` — procedura deterministica di pubblicazione
  e verifica.

Esempio riproducibile, con SHA e istante UTC espliciti:

```powershell
python tools/publish_from_mox_core.py `
  --source-dir C:\percorso\mox-core\meta `
  --source-commit <sha-completo-mox-core> `
  --generated-at 2026-09-19T00:00:00Z

python tools/publish_from_mox_core.py `
  --source-dir C:\percorso\mox-core\meta `
  --source-commit <sha-completo-mox-core> `
  --generated-at 2026-09-19T00:00:00Z `
  --check
```

Le due run si fermano con esito diverso da zero anche quando in `meta/` resta un
catalogo che la sorgente non ha piu': un artefatto generated-only non deve
sopravvivere alla propria sorgente. Lo strumento lo segnala e la rimozione la
decide chi pubblica.

Ogni mazzo porta **la fonte e la data** da cui e' stato preso. Dove un dato non
esiste c'e' scritto `n.d.`: in questo progetto non si inventano numeri.

Il campo `tier` e' il **Mox Tier**, da 1 a 4. I livelli 1, 2 e 3 arrivano da una
tier list esterna e portano sempre accanto `tier_fonte`, `tier_data` e
`tier_archetipo`. Il livello 4 vuol dire **non classificato da una fonte
verificata**, non «mazzo scarso»: e' il modo di dire «non lo so» senza lasciare
un buco.

## Da dove vengono le liste

Da fonti pubbliche, indicate mazzo per mazzo nel campo `fonte`. Per legalita',
rotazioni e carte bandite l'autorita' e' Wizards of the Coast; per il metagame
si usano fonti pubbliche che lo misurano.

Alcune liste hanno come fonte la parola **`costruita`**: sono liste messe
insieme per Mox a partire da un archetipo che una fonte cita ma di cui non
pubblica le sessanta carte. Passano gli stessi controlli di legalita' delle
altre, ma non sono la decklist di nessuno, e c'e' scritto: mettere l'indirizzo
dell'archetipo nel campo `fonte` farebbe credere che quel sito abbia
pubblicato la lista.

Prima di pubblicare, ogni lista passa da un validatore che controlla contro il
client di Arena: set legali, carte bandite, dimensioni esatte, singleton e
limite di copie sulla somma fra mazzo e riserve. Le liste che non superano il
controllo non vengono pubblicate, e quelle che diventano illegali vengono
ritirate invece che corrette a indovinare.

I nomi delle carte, i simboli e le illustrazioni di Magic: The Gathering sono
di Wizards of the Coast. Qui non c'e' nessun contenuto del gioco: solo elenchi
di nomi di carte, come una lista della spesa.
