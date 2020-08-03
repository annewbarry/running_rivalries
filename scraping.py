import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pymongo import MongoClient

import pprint
# Requests sends and recieves HTTP requests.
import requests

# Beautiful Soup parses HTML documents in python.
from bs4 import BeautifulSoup

import json

'''
List of urls to scrape from
'''
urls_list = [['https://results.nyrr.org/event/M2019/finishers#g=M&page=1&af=40&at=44', 'Men 40-44', 'Mar'], ['https://results.nyrr.org/event/M2019/finishers#g=M&page=1&af=45&at=49', 'Men 45-49', 'Mar'], ['https://results.nyrr.org/event/M2019/finishers#g=F&page=1&af=25&at=29', 'Women 25-29', 'Mar'], ['https://results.nyrr.org/event/M2019/finishers#g=F&page=1&af=30&at=34', 'Women 30-34', 'Mar'], ['https://results.nyrr.org/event/5AV-19/finishers#g=F&page=1&af=25&at=29', 'Women 25-29', 'Mile'], ['https://results.nyrr.org/event/5AV-19/finishers#g=F&page=1&af=30&at=34', 'Women 30-34', 'Mile'],['https://results.nyrr.org/event/5AV-19/finishers#g=M&page=1&af=40&at=44', 'Men 40-44', 'Mile'], ['https://results.nyrr.org/event/5AV-19/finishers#g=M&page=1&af=45&at=49', 'Men 45-49', 'Mile']]

'''
sets up MongoDB
'''
# client = MongoClient('localhost', 27017)
# racing = client['results']
# source = racing['source code']
# runners = racing['indiv']

client = MongoClient('localhost', 27017)
racing = client['sunday']
source = racing['source code']
runners = racing['indiv']

def parse_results(data, distance, ag):
  '''
    Uses BeautifulSoup to parse HTML and populates a MongoDB with the
    name, finish time, age, age group, and distance of each runner
    from a results page

    Parameters:
    ----------
    data :
      page source for a set of NYRR race results
    distance: the distance of the race (string)
    ag:
      the age group for the results (string). Example: 'Men 40-44'


    Returns:
    ----------
    None
  '''
  soup = BeautifulSoup(data, 'html.parser')
  for i, result in enumerate(soup.findAll("div",'rms-grid-item')):
    t = result.findAll("span", "long-text")[0].text[4:]
    a = int(result.findAll("span", "ng-binding ng-scope")[0].text[1:])
    n = result.findAll('div', 'name rms-grid-line ng-binding')[0].text.strip()
    runners.insert({'name': n, 'time':t, 'age': a, 'ag': ag, 'dist': distance})


def scrape(url):
  '''
    Takes a url and scrapes the page source using selenium

    Parameters:
    ----------
    url:
      a string of a url


    Returns:
    ----------
    source: page source code
  '''
def scrape(url):
  chrome_driver_path = "/Users/annebarry/galvanize/running_rivalries/chromedriver"
  driver = webdriver.Chrome(executable_path = chrome_driver_path)
  driver.get(url)
  time.sleep(10)
  button = driver.find_elements_by_class_name('button-load-more')
  while True:
    try:
      button[1].click()
      time.sleep(12)
    except:
      break
  source = driver.page_source
  return source

if __name__ == '__main__':
  '''
    scrapes each url in urls_list, stores the page source
    in the race_results collection, then parses the information
    about each runner

    Parameters:
    ----------
    url:
      a string of a url


    Returns:
    ----------
    None
  '''
  for i in range(len(urls_list)):
    source_code = scrape(urls_list[i][0])
    print(urls_list[i][0])
    racing.source.insert({'name': urls_list[i][1], 'source': source_code})
    parse_results(source_code, urls_list[i][2], urls_list[i][1])