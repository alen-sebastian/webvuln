import re
from urllib.parse import urlparse, parse_qs

param_regex = re.compile(r'https?://[^/]+/[^?]*\?([^&=]+)=')
blacklist_regex = re.compile("|".join(blacklist)) 

def param_extract(response, level, blacklist, placeholder):

  params = set()
  
  for url in response.split('\n'):
    if any(bl_word in url for bl_word in blacklist):
      continue
      
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    
    for param in query:
      if level == 'high':
        params.add(f"{param}={placeholder}")  
      else:
        params.add(f"{param}=")
              
  return list(params)

# Example
response = "http://example.com?p1=123&p2=456...." 

final_params = param_extract(response, 'high', ['png', 'jpg'], 'XXX')

print(final_params)
