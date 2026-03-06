import argparse
import json
import csv
import sys
import os

def json_to_csv(json_file_path, csv_file_path):
    print(f"Inizio conversione di {json_file_path} in {csv_file_path}...")
    
    try:
        # Apri i file
        with open(json_file_path, 'r', encoding='utf-8') as infile, \
             open(csv_file_path, 'w', encoding='utf-8', newline='') as outfile:
            
            # Inizializza il writer CSV riga per riga dal JSON
            writer = None
            
            # Scorrimento riga per riga
            for i, line in enumerate(infile):
                line = line.strip()
                if not line:
                    continue
                    
                try:
                    data = json.loads(line)
                except json.JSONDecodeError:
                    print(f"Errore di decodifica JSON alla riga {i+1}. Ignorata.")
                    continue
                    
                # Scrivi gli header alla prima riga valida
                if writer is None:
                    headers = list(data.keys())
                    writer = csv.DictWriter(outfile, fieldnames=headers)
                    writer.writeheader()
                    
                writer.writerow(data)
                
                # Progress bar ogni 500,000 righe
                if (i + 1) % 500000 == 0:
                    print(f"Elaborate {i + 1} righe...")

        print(f"Conversione completata con successo! Il file salvato è: {csv_file_path}")
    except Exception as e:
        print(f"Errore durante l'elaborazione del file: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Converti in modo efficiente un file JSON Lines in formato CSV.")
    parser.add_argument("input", help="Percorso del file JSON di input")
    parser.add_argument("output", help="Percorso del file CSV di output")
    
    args = parser.parse_args()
    
    if os.path.exists(args.input):
        json_to_csv(args.input, args.output)
    else:
        print(f"Errore: Il file {args.input} non esiste.")
        sys.exit(1)
