from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import mysql.connector
import datetime
import requests
import os


image_directory = f"< add path >"
table = f"< add path >"


def scrape_website(url, element_class):
    # Connect to the database
    conn = mysql.connector.connect(
        host=" ", user=" ", password=" ", database=" "
    )
    c = conn.cursor()

    # Create the table if it doesn't exist
    c.execute("CREATE TABLE IF NOT EXISTS sport(title TEXT, article TEXT, date DATE)")

    # Change the path of the browser
    driver = webdriver.Firefox(
        executable_path="< add path >"
    )

    # Load the webpage
    driver.get(url)
    the_title = []
    the_article = []
    the_data = []
    # Get the current date
    today = datetime.datetime.today().date()
    the_data.append(today)
    # Get the page source and parse it with Beautiful Soup
    content = driver.page_source
    soup = BeautifulSoup(content)
    driver.quit()

    # Find all the div elements with the specified class
    for div in soup.findAll(class_=element_class):
        # Find the h1 element within the div
        title = div.find("h1")
        # Find all the p elements within the div
        paragraphs = div.find_all("p")
        # Concatenate the text of the p elements into a single string
        article = "\n".join([p.text for p in paragraphs])
        # Check if the h1 element exists and hasn't been added to the result list yet
        if title:
            c.execute(
                """INSERT INTO sport(title, article, date) VALUES(%s, %s, %s)""",
                (title.text, article, today),
            )
            the_title.append(title.text)
            the_article.append(article)

        # Find all the images within the div
        images = div.find_all("img")
    # Iterate over the images and download them
    for i, image in enumerate(images):
        # Get the image URL
        image_url = image["src"]
        # Download the image
        response = requests.get(image_url)
        # Save the image to a file with a unique filename
        image_path = os.path.join(image_directory, f"image_{i}.jpg")
        open(image_path, "wb").write(response.content)

    # Save the results to a CSV file
    df = pd.DataFrame({"title": the_title, "article": the_article, "date": the_data})
    df[["title", "article", "date"]].to_csv(table, index=False, encoding="utf-8")

    # Commit the changes to the database and close the connection
    conn.commit()
    conn.close()


scrape_website(
    "< add url >",
    "< add class name >",
)
