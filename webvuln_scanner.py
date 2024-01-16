#!/usr/bin/env python3

import argparse
import csv
import json
import os
import subprocess
from datetime import datetime
from threading import Thread 

def scan_target(target, output_file):
    subprocess.run(["nikto", "-h", target, "-o", output_file]) 

def parse_results(output_file):
    vulnerabilities = []
    with open(output_file, "r") as f:
        for line in f:
            if "OSVDB" in line:
                vuln_id, vuln_desc = line.strip().split ["- "]
                vulnerabilities.append((vuln_id, vuln_desc))
    return vulnerabilities
                
def main():

    parser = argparse.ArgumentParser(description="Advanced website vulnerability scanner using Nikto")
    parser.add_argument("target", help="Target website URL")
    parser.add_argument("-j", "--json", action="store_true", help="Output results to JSON") 
    parser.add_argument("-c", "--csv", action="store_true", help="Output results to CSV")
    args = parser.parse_args()

    target = args.target
    output_file = f"{target}_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    
    print(f"Scanning {target}...")
    
    
    thread = Thread(target=scan_target, args=(target, output_file))
    thread.start()
    thread.join()

    vulnerabilities = parse_results(output_file)

    if args.json:
        print(json.dumps(vulnerabilities, indent=4))
    elif args.csv:
        csv_writer = csv.writer(sys.stdout)
        csv_writer.writerow(["Vulnerability ID", "Description"])        
        csv_writer.writerows(vulnerabilities)        
    else: 
        print(f"\nVulnerabilities identified for {target}:")
        for vuln in vulnerabilities:
            print(f"{vuln[0]}: {vuln[1]}")
            
    os.remove(output_file)

if __name__ == "__main__":
    main()
