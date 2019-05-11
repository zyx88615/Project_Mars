from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrapemars
import pandas as pd

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/Mars_app"
mongo = PyMongo(app)



# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def Lastest_Mars_News():
    News_data = mongo.db.lastest.find_one()
    Featured_data = mongo.db.Featured.find_one()
    Weather_data = mongo.db.Weather.find_one()
    Hemisphere_data = mongo.db.Hemisphere.find_one()
    Table_data = scrapemars.scrape4()
    TableHtml=Table_data.to_html(classes="data")




    return render_template("index.html", latest=News_data,Featured=Featured_data,\
    						Weather=Weather_data, Hemisphere=Hemisphere_data,\
                            tables=[TableHtml])





@app.route("/scrape")
def scrape():

    # Run the scrape function
    latest_news = scrapemars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.lastest.update({}, latest_news , upsert=True)


    Featured_address= scrapemars.scrape1()
    mongo.db.Featured.update({}, Featured_address,  upsert=True)

    weather_info = scrapemars.scrape2()
    mongo.db.Weather.update({}, weather_info,  upsert=True)

    Hemisphere_address= scrapemars.scrape3()
    mongo.db.Hemisphere.update({}, Hemisphere_address,  upsert=True)


    # Redirect back to home page
    return redirect("/")






if __name__ == "__main__":
    app.run(debug=True)