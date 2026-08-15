# mox-meta — le liste dei mazzi di Mox

Questo deposito contiene **soltanto le liste dei mazzi** che
[Mox](https://github.com/Dennis96) usa per il consigliere. Niente codice,
niente dati personali: 7 file per 91 mazzi in 7 formati,
circa 155 KB in tutto.

Serve a una cosa sola: **le liste invecchiano e il programma no**. Quando esce
un set o arrivano delle carte bandite, Mox scarica da qui i file aggiornati
invece di far reinstallare tutto il pacchetto da 54 MB.

L'aggiornamento del 15 agosto 2026 concentra la copertura soprattutto su
**Standard e Standard BO1**: `meta/standard.json` contiene 26 mazzi, di cui
17 BO1 e 9 BO3. Le liste Standard sono state ricontrollate contro la banned
list vigente; una lista che contiene una carta bandita non viene mantenuta solo
perche' era forte o popolare prima del ban.

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
- `meta/*.json` — un file per formato: Standard, Alchemy, Explorer, Historic,
  Timeless, Brawl e Historic Brawl.

Ogni mazzo porta **fonte e data**. Quando la lista e' stata presa da una
specifica decklist pubblica, `fonte` punta a quella decklist. Le poche voci il
cui campo `perche` dichiara esplicitamente **"variante Mox"** sono invece
varianti interne costruite per rappresentare un archetipo documentato dalla
fonte indicata: non vengono presentate come copie di una decklist esterna e
passano gli stessi controlli di legalita'. Dove un dato come tier o winrate non
esiste, resta `n.d.`/`null`: in questo progetto non si inventano numeri.

## Da dove vengono le liste

Le fonti vengono indicate mazzo per mazzo. Per legalita', rotazioni e ban la
fonte di riferimento e' Wizards of the Coast; per il metagame vengono usate
anche fonti pubbliche come MTGA Assistant, AetherHub e MTGDecks quando sono
utili a documentare archetipi e liste giocate realmente.

Prima di pubblicare, il catalogo viene controllato per formato: dimensione
minima del mazzo, sideboard, limite di copie, singleton dove previsto, carte
bandite e carte limitate. Per Standard viene verificato inoltre che le liste
provengano da uno Standard ancora valido: nel 2026 non c'e' una nuova rotazione,
quindi per le liste che erano Standard nel 2026 il controllo successivo si
concentra soprattutto sui nuovi ban e sulla legalita' corrente del formato.
Le liste che non superano i controlli vengono ritirate invece che corrette a
indovinare.

I nomi delle carte, i simboli e le illustrazioni di Magic: The Gathering sono
di Wizards of the Coast. Qui non c'e' nessun contenuto del gioco: solo elenchi
di nomi di carte, come una lista della spesa.
