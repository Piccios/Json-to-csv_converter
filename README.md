# Fast JSONL to CSV Converter

Uno script in Python leggero, veloce ed estremamente efficiente per convertire enormi file JSON (formattati come JSON Lines/NDJSON) in file CSV. Elabora i file riga per riga, risultando ottimizzato per minimizzare l'utilizzo della memoria RAM.

## Caratteristiche

- **Ottimizzato per la Memoria**: Elabora i dati "streammando" riga per riga senza cercare di caricare l'intero file in memoria RAM. Ideale per file molto pesanti (es. dataset da svariati GB).
- **Facilità d'Uso**: Semplice interfaccia a riga di comando (CLI).
- **Resiliente agli Errori**: Identifica, cattura e ignora eventuali righe con JSON malformati per continuare l'elaborazione del resto del dataset.
- **Zero Dipendenze**: Lo script è scritto in puro Python (>= 3.6). Usa solo moduli della core library (`json`, `csv`, `os`, `sys`, `argparse`).
- **Supporto UTF-8**: Mantiene in modo corretto l'encoding per i caratteri di testo speciali.

## Installazione

Nessuna installazione richiesta se hai già Python sul tuo sistema! È sufficiente clonare questa repository o scaricare il file `convert.py`.

```bash
git clone https://github.com/Piccios/Json-to-csv_converter.git
cd Json-to-csv_converter
```

## Utilizzo

Lo script richiede semplicemente 2 parametri passati a linea cdi comando: l'input JSON e l'output CSV desiderato.

```bash
python convert.py <input.json> <output.csv>
```

### Esempio

```bash
python convert.py IT-file_2026-02.json IT-file_2026-02.csv
```

Un output simile verrà generato sulla console (se il salvataggio è per grandi quantitativi di dati):

```text
Inizio conversione di IT-file_2026-02.json in IT-file_2026-02.csv...
Elaborate 500000 righe...
Elaborate 1000000 righe...
Elaborate 1500000 righe...
Conversione completata con successo! Il file salvato è: IT-file_2026-02.csv
```

Puoi richiamare sempre i messaggi di help dello script eseguendo:

```bash
python convert.py -h
```

## Struttura del file JSON analizzato

Lo script si aspetta file d'ingresso formattati secondo lo standard [JSON Lines (JSONL)](https://jsonlines.org/). Questo significa che ogni riga del tuo file deve corrispondere a un oggetto JSON indipendente e valido.

**Esempio di input compatibile:**
```json
{"nome": "Mario", "cognome": "Rossi", "eta": 30}
{"nome": "Luca", "cognome": "Verdi", "eta": 25}
{"nome": "Giulia", "cognome": "Bianchi", "eta": 28}
```
*Attenzione: un file colmo di enormi Array JSON classici (es. `[{}, {}, {}]`) richiederà un parser diverso da quello offerto da questo convertitore riga per riga.*

## Come Contribuire

Sentiti libero di aprire issue e pull request se desideri aggiungere controlli per l'input o lanciare nuove migliorie!
