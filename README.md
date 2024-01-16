# webvuln_scanner

WebVulnScanner is a Python tool to scan websites for vulnerabilities using Nikto. 

## Installation

```bash
pip install webvuln_scanner
```

## Usage

```bash
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

This will scan example.com and output results to results.csv in CSV format.

## Output

### Text

Prints detected vulnerabilities with OSVDB IDs:

```
OSVDB-3092: /test/: Potentially interesting directory w/ listing on 'apache/2.4.6 (centos)'
OSVDB-3268: /icons/: Directory indexing found.
OSVDB-3500: /tmp/: Directory indexing found.
``` 

### CSV 

Vulnerabilities in CSV format with columns for ID and description:

```
OSVDB-3092,/test/: Potentially interesting directory w/ listing on 'apache/2.4.6 (centos)'
OSVDB-3268,/icons/: Directory indexing found. 
OSVDB-3500,/tmp/: Directory indexing found.
```

### JSON

Vulnerabilities in JSON format:

```json
[
  {
    "id": "OSVDB-3092",
    "description": "/test/: Potentially interesting directory w/ listing on 'apache/2.4.6 (centos)'"
  },
  {
    "id": "OSVDB-3268",
    "description": "/icons/: Directory indexing found."
  },
  {
    "id": "OSVDB-3500", 
    "description": "/tmp/: Directory indexing found."
  }
]
```

## Contributing

Contributions welcome! Please create an issue or PR on GitHub.
