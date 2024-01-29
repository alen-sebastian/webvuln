import threading 
from queue import Queue
from html.parser import HTMLParser  
from urllib.request import urlopen
from urllib import parse


class CrawlerThread(threading.Thread):

  def __init__(self, queue):
    threading.Thread.__init__(self)
    self.queue = queue

  def run(self):
    while True:
      url = self.queue.get()
      self.crawl_page(url)
      self.queue.task_done()

  def crawl_page(self, url):
    try:
      parser = LinkParser()
      data, links = parser.getLinks(url)
      for link in links:
        if is_valid(link):
          self.queue.put(link) 
    except:
      pass

# Other crawler code 

def spider(url, max_threads, max_depth):
  
  root_url = url
  domain = root_url.split("/")[2]
  visited = set() 
  queue = Queue()
  queue.put((url, 0)) # url, depth

  for i in range(max_threads):
    t = CrawlerThread(queue)
    t.setDaemon(True)
    t.start()

  queue.join()
  return list(visited) 

def is_valid(url):
  # Filter logic
  return True 

print(spider("http://example.com", 10, 1))
