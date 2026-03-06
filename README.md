# Fast JSONL to CSV Converter

Hey fellow developers! I built this lightweight Python script to solve a common headache: converting massive JSON files (specifically JSON Lines/NDJSON) into CSV formats without crashing our machines.

I hope this saves you some valuable time!

## ✨ Features

- **Memory Optimized**: Streams data line-by-line rather than loading the whole file into RAM. Perfect for those massive, multi-GB datasets you need to crunch.
- **Dead Simple Usage**: Just a clean, straightforward Command Line Interface (CLI).
- **Error Resilient**: Bad JSON formatting on line 42,069? No problem. The script catches malformed lines, logs them, and keeps processing the rest of your dataset.
- **Zero Dependencies**: Written in pure Python (>= 3.6). It only relies on core library modules (`json`, `csv`, `os`, `sys`, `argparse`), so you don't need a messy `requirements.txt`.
- **UTF-8 Support**: Properly handles special characters and text encoding right out of the box.

## 🚀 Installation

If you have Python on your machine, you're already good to go—no `pip install` required! Just clone the repo or grab the `convert.py` file.

```bash
git clone https://github.com/Piccios/Json-to-csv_converter.git
cd Json-to-csv_converter
```

## 💻 Usage

The script just needs two simple arguments: your input JSON file and where you want to save the output CSV.

```bash
python convert.py <input.json> <output.csv>
```

### Example

```bash
python convert.py IT-file_2026-02.json IT-file_2026-02.csv
```

While it runs (especially on huge datasets), it'll give you progress updates so you know it hasn't frozen:

```text
Inizio conversione di IT-file_2026-02.json in IT-file_2026-02.csv...
Elaborated 1000 rows...
Elaborated 2000 rows...
Elaborated 3000 rows...
Conversion completed successfully! The file saved is: IT-file_2026-02.csv
```

Forgot the commands? You can always pull up the help menu:

```bash
python convert.py -h
```

## 📄 Expected JSON Structure

This script expects input files formatted as [JSON Lines (JSONL)](https://jsonlines.org/). This simply means each line of your file must be its own independent, valid JSON object.

**Compatible Input Example:**
```json
{"name": "Mario", "surname": "Rossi", "age": 30}
{"name": "Luca", "surname": "Verdi", "age": 25}
{"name": "Giulia", "surname": "Bianchi", "age": 28}
```
*Heads up: If your file is just one giant standard JSON Array (e.g., `[{}, {}, {}]`), this specific line-by-line parser won't work for it.*

## 🤝 Contributing

We made this tool to make developers' lives easier. If you want to add input validation, new features, or just make it better, feel free to open an issue or drop a pull request!
