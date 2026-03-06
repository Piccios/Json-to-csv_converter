import argparse
import json
import csv
import sys
import os

def json_to_csv(json_file_path, csv_file_path):
    print(f"Starting conversion of {json_file_path} to {csv_file_path}...")
    
    try:
       
        with open(json_file_path, 'r', encoding='utf-8') as infile, \
             open(csv_file_path, 'w', encoding='utf-8', newline='') as outfile:
            
            writer = None
            
            for i, line in enumerate(infile):
                line = line.strip()
                if not line:
                    continue
                    
                try:
                    data = json.loads(line)
                except json.JSONDecodeError:
                    print(f"Errore di decodifica JSON alla riga {i+1}. Ignorata.")
                    continue
                    
                if writer is None:
                    headers = list(data.keys())
                    writer = csv.DictWriter(outfile, fieldnames=headers)
                    writer.writeheader()
                    
                writer.writerow(data)
                
                # Progress bar every 1000 rows
                if (i + 1) % 1000 == 0:
                    print(f"Elaborated {i + 1} rows...")

        print(f"Conversion successfully completed! The file saved is: {csv_file_path}")
    except Exception as e:
        print(f"Error during file processing: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a JSON Lines file to CSV in an efficient way.")
    parser.add_argument("input", help="Path to the input JSON file")
    parser.add_argument("output", help="Path to the output CSV file")
    
    args = parser.parse_args()
    
    if os.path.exists(args.input):
        json_to_csv(args.input, args.output)
    else:
        print(f"Error: The file {args.input} does not exist.")
        sys.exit(1)
