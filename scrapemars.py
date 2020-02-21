from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pandas as pd
from flask import jsonify
from bson import json_util, ObjectId
import json
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    

    return Browser("chrome")


def scrape():
    browser = init_browser()
    lastest = {}

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"    

    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('div', class_="content_title")
    header = soup.find("div", class_="rollover_description_inner")

    lastest["title"] = title.text.strip()
    lastest["header"] = header.text.strip()
    browser.quit()

    return json.loads(json_util.dumps(lastest))

def scrape1():
    browser = init_browser()
    featured_img_address={}
    baseurl="https://www.jpl.nasa.gov"
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    temp_address = soup.find('a', class_="button fancybox")
    temp_address = temp_address["data-fancybox-href"]
    featured_img_address["Address"] = baseurl+temp_address
    browser.quit()

    return json.loads(json_util.dumps(featured_img_address))


def scrape2():
    weather={}
    url= "https://twitter.com/marswxreport?lang=en"
	response = requests.get(url)
	soup1 = BeautifulSoup(response.text, 'lxml')
	findtwit = soup1.find('p',class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
	findtwit=findtwit.strip("")[8:-26]
	weather["info"]=findtwit.replace("\n", ", ")

    return json.loads(json_util.dumps(weather))

def scrape3():
    browser = init_browser()
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    try:
        findtimg = soup.find_all('img',class_="thumb")
    except AttributeError:
        findtimg =None

    baseurl= "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/"
    browser.quit()
    ddd=[]
    for x in findtimg:
       ddd.append(baseurl+x["src"][47:-10]+"/full.jpg")
    Hemi={}
    Hemi["address"]=ddd
    return json.loads(json_util.dumps(Hemi))

def scrape4():
    url="https://space-facts.com/mars/"
    tables = pd.read_html(url)
    df=tables[2]
    df.columns=["Description","Values"]
    df.set_index("Description", inplace=True)
    df1=df.to_html(classes="data")
    return json.loads(json_util.dumps(df1))