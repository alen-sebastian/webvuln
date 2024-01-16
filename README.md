# webvuln_scanner 

WebVulnScanner is a Python vulnerability scanner utilizing Nikto.

## Installation

```bash
git clone https://github.com/alen-sebastian/webvuln.git
cd webvuln 
python setup.py install
```

Or install via pip:

```bash 
pip install git+https://github.com/alen-sebastian/webvuln.git
```

## Usage

```
webvuln_scanner [options] <url>
```

**Options:**

`-o, --output <file>` - Output file for results (default: `results.txt`)

`-f, --format <format>` - Output format: text, csv, json (default: text) 

`-t, --threads <num>` - Number of threads (default: 5)

## Example 

```
webvuln_scanner -o results.csv -f csv https://example.com
```

Scans example.com and saves CSV results to results.csv.

## Output Formats

### Text

Prints vulnerabilities with OSVDB IDs:

```
OSVDB-3092: /test/: Potentially interesting directory  
OSVDB-3268: /icons/: Directory indexing found.
```

### CSV

```
OSVDB-3092,/test/: Potentially interesting directory
OSVDB-3268,/icons/: Directory indexing found.  
```

### JSON 

```json
[
  {
    "id": "OSVDB-3092",
    "description": "/test/: Potentially interesting directory"
  },
  {  
    "id": "OSVDB-3268",
    "description": "/icons/: Directory indexing found."
  }
]
```

## Contributing

Contributions welcome! Please create an issue or PR on GitHub. 
