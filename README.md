# mox-meta — le liste dei mazzi di Mox

Questo deposito contiene **soltanto le liste dei mazzi** che
[Mox](https://github.com/Dennis96) usa per il consigliere. Niente codice,
niente dati personali: 7 file per 71 mazzi in 7 formati,
129 KB in tutto.

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
- `meta/*.json` — un file per formato: Standard, Alchemy, Explorer, Historic,
  Timeless, Brawl e Historic Brawl.

Ogni mazzo porta **la fonte e la data** da cui e' stato preso. Dove un dato non
esiste c'e' scritto `n.d.`: in questo progetto non si inventano numeri.

## Da dove vengono le liste

Da fonti pubbliche, indicate mazzo per mazzo nel campo `fonte`. Prima di
pubblicare, ogni lista passa da un validatore che controlla contro il client di
Arena: set legali, carte bandite, dimensioni esatte, singleton e limite di
copie sulla somma fra mazzo e riserve. Le liste che non superano il controllo
non vengono pubblicate, e quelle che diventano illegali vengono ritirate invece
che corrette a indovinare.

I nomi delle carte, i simboli e le illustrazioni di Magic: The Gathering sono
di Wizards of the Coast. Qui non c'e' nessun contenuto del gioco: solo elenchi
di nomi di carte, come una lista della spesa.
