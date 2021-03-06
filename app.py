from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scraping  # import scraping.py

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
# Connect to Mongo and select mars_app Database and NOT A COLLECTION!!!!
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# To see the DB


@app.route("/")
def index():
    # Use PyMongo to find the 'mars' collection in the database and assgin the path to variable mars
    mars = mongo.db.mars.find_one()
    # Render the mongo data in the HTML index
    return render_template("index.html", mars=mars)

# To update the DB


@app.route("/scrape")
def scrape():
    mars = mongo.db.mars  # access the database, scrape new data using our scraping.py
    mars_data = scraping.scrape_all()  # the function scrap_all() works on scraping.py
    mars.update({}, mars_data, upsert=True)
    return redirect('/', code=302)


# run flask
if __name__ == "__main__":
    app.run()
