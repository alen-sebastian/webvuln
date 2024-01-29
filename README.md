 Here is a sample README.md file I would create for the web vulnerability scanner code:

# Web Vulnerability Scanner

This tool scans websites for common web vulnerabilities like XSS, SQLi, etc. 

## Features

- Crawls a target domain to find pages to test
- Extracts URLs and parameters from the crawl 
- Tests for SQL injection vulnerabilities by injecting payloads
- Checks for reflected XSS in parameters
- Can scan subdomains or a single domain
- Output reports found vulnerabilities

## Usage

```
# Crawl example.com
python scanner.py -d example.com

# Crawl subdomains of example.com 
python scanner.py -d example.com -s True

# Output results to file
python scanner.py -d example.com -o results.txt  
```

## Installation

```
git clone https://github.com/user/scanner.git](https://github.com/alen-sebastian/webvuln.git
pip install -r requirements.txt
```

Requires Python 3 and the following libraries:

- requests
- BeautifulSoup
- optparse

## Customizing

The `payloads.txt` file contains the list of SQLi and XSS payloads to test. You can add or modify payloads to customize for your needs.

## Contributing

Contributions to the scanner are welcome! Please open issues or PRs on Github.

Potential areas of contribution:

- Adding other vulnerability checks like LFI, RCE, etc
- Expanding crawler functionality
- Improving output reporting
- Performance optimization
