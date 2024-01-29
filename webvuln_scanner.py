import requests
import re
import argparse
import os
import time
from urllib.parse import unquote
from tqdm import tqdm

cached_archive_resp = None
compiled_regexes = {}
payloads = []

def clear():
  if 'linux' in sys.platform:
    os.system('clear')
  elif 'darwin' in sys.platform: 
    os.system('clear')
  else:
    os.system('cls')

def get_archive_urls(domain, subs):
  global cached_archive_resp
  if cached_archive_resp is None:
    url = f"http://web.archive.org/cdx/search/cdx?url=*.{domain}/*&output=txt&fl=original&collapse=urlkey&page=/" if subs else f"http://web.archive.org/cdx/search/cdx?url={domain}/*&output=txt&fl=original&collapse=urlkey&page=/"
    cached_archive_resp = unquote(requests.get(url).text)
  return cached_archive_resp

def test_payloads(uris):
  vuln_urls = []
  with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(test_uri, uri) for uri in uris]
    for future in tqdm(as_completed(futures), total=len(futures)):
      if future.result():
        vuln_urls.append(future.result())
  return vuln_urls

def test_uri(uri):
  for payload in payloads:
    final_url = f"{uri}{payload}"
    try:
      req = requests.get(final_url)
      if 'SQL' in req.text:
        return final_url
    except:
      pass
  return None

def main():
  parse_args()
  clear()
  archive_resp = get_archive_urls(args.domain, args.subs)
  urls = extractor.param_extract(archive_resp, 'high', ['woff','js','ttf'], compiled_regexes)
  with open('payloads.txt', 'r') as f:
    payloads = f.read().splitlines()
  vuln_urls = test_payloads(urls)
  print_results(vuln_urls)

if __name__ == "__main__":
  main()
