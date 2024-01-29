import requests
from requests.exceptions import RequestException

def connector(url):

  try:
    headers = {'User-Agent': get_random_user_agent()}
    response = requests.get(url, headers=headers, timeout=30)
    return response.text
  
  except RequestException as e:
    print(f"Error fetching URL: {e}")
    return None

# User agent utils
user_agents = [] # populate list 

def get_random_user_agent():
  return random.choice(user_agents)
