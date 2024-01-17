#!/usr/bin/env python3

import argparse
import multiprocessing
import subprocess
import os
import re

import requests
from bs4 import BeautifulSoup

# Nikto program and database location 
NIKTO_EXE = "/usr/bin/nikto"
NIKTO_DB = "/usr/share/nikto/plugins/nikto_db"

def scan_target(target):
    """Run Nikto scan on target"""
    output = subprocess.check_output([NIKTO_EXE, "-host", target, "-db", NIKTO_DB])
    return output.decode()

def parse_results(output):
    """Extract results from Nikto output"""
    vulns = []
    pattern = re.compile(r"OSVDB-(\d+): (.*)")
    
    for line in output.splitlines():
        match = pattern.match(line)
        if match:
            vulns.append(match.groups())
            
    return vulns

def get_vuln_details(vuln_id):
    """Scrape OSVDB website for vulnerability details"""
    url = f"https://vuldb.com/?{vuln_id}"
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extract vulnerability description from page
        desc = soup.find("div", id="vuln-desc").text 
        return desc
        
    except Exception as e:
        print(f"Error scraping vulnerability details: {e}")
        
def print_results(target, vulns):
    """Output results to console"""
    
    print(f"Vulnerabilities found for {target}:")
    
    for vuln_id, desc in vulns:
        # Enhance basic description with scraped details
        full_desc = desc + " " + get_vuln_details(vuln_id)
        print(f"{vuln_id}: {full_desc}")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("target")
    args = parser.parse_args()

    target = args.target
    
    # Run Nikto scan 
    output = scan_target(target)
    
    # Parse output for vulnerabilities
    vulns = parse_results(output)

    # Print results
    print_results(target, vulns)
