import multiprocessing as mp 
import argparse
import csv
import re
from io import StringIO

vuln_pattern = re.compile(r'OSVDB-(\d+): (.*)')

def scan_target(target):
    
    return subprocess.check_output(["nikto", "-h", target])

def parse_results(output):
     
    for line in output.splitlines():
        match = vuln_pattern.search(line)
        if match:
            yield match.groups()

def print_results(results):
    
    for vuln_id, desc in results:
        print(f"{vuln_id}: {desc}")

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("target")
    args = parser.parse_args()
    
    
    output = scan_target(args.target) 
    
     
    with mp.Pool() as pool:
        results = pool.map(parse_results, [output])
    
     
    print_results(results)
    
if __name__ == "__main__":
    main()
