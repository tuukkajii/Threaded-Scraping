import json
import requests
from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulSoup
import argparse
import thread
import sys
def run(start, end):
    starts = start
    f = open('output.text', 'r+')
    f.truncate()
    f.close()
    start = end - start
    ds = start /4
    dsa = ds
    m = ds * 4
    t = start - m
    if m != start:
        ds2 = dsa + t
        scrape1 = start - ds2
    else:
        scrape1 = starts + ds 
    scrape2 = scrape1 + ds
    scrape3 = scrape2 + ds
    scrape4 = scrape3 + ds
    ends = end + 1
    list1 = []
    try:       
        thread.start_new_thread( get_id, (starts, scrape1,list1) )
        thread.start_new_thread( get_id, (scrape1, scrape2,list1) )
        thread.start_new_thread( get_id, (scrape2, scrape3,list1) )
        thread.start_new_thread( get_id, (scrape3, ends,list1) )       
    except:
        print "Error: unable to start thread"
    while 1:
        pass


def get_id(start, end,list1):
  f = open('output.text', 'a')
  i = start
  while (i < end):
    try:
      base_url = ('https://www.back-door.it/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwww.back-door.it%2F?p=' + str(i))
      r = requests.get(base_url)
      c = json.loads(r.text)
      l= ("\n" + str(i) + "  :  " + c['title'])
      f.write(l)
      i = i + 1
    except Exception:
      l = ("\n" + str(i)+ "  :  Exception")
      f.write(l)
      i = i+1

     
      
if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='backdoor.it scraper')

  parser.add_argument('-s', '--start', required=True,
      type=int,
      help="start pid")

  parser.add_argument('-e', '--end', required=True,
      type=int,
      help="end pid")

  args = parser.parse_args()

  run(args.start, args.end)
