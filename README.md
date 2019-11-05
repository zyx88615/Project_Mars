# MISSION TO MARS

App is using chrome web-driver and MongoDB Atlas database, successfully deployed to Heroku.


![](image/1.png)
![](image/2.png)
![](image/3.png)

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.



## Getting started
* Start by converting your Jupyter notebook into a Python script called `scrapemars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

* Next, create a route called `/scrape` that will import your `scrapemars.py` script and call your `scrape` function.

* Store the return value in Mongo as a Python dictionary.

* Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.

* Click on the "Scrape New Data" button

## Author

Neal Zheng
