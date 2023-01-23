Web Scraper 

This is a Python script that uses Selenium and Beautiful Soup to scrape articles from any website, save the articles to a MySQL database and also save the images to a local folder and the title, article and date to a local file.
Requirements

    Python 3.x
    Selenium
    Beautiful Soup
    Pandas
    mysql.connector
    requests
    os

Installation

To use this script, you will need to have the following software installed on your machine:

    Firefox browser
    geckodriver.exe
    MySQL server

You will also need to install the required Python packages. You can do this by running the following command:

pip install selenium beautifulsoup4 pandas mysql-connector-python requests

Usage

    Create a database with a name of your choice.
    Change the path of the browser in the script to match the path of your geckodriver.exe file on your machine.
    Update the conn = mysql.connector.connect(host="", user="", password="", database="") variable in the script to match the host, user, password, and the name of the database you created
    Update the image_directory = f"path_to_your_image_folder" and table = f"path_to_your_article_text_file" variables in the script to match the local paths on your machine where you want the images and article.txt file to be saved.
    The script takes two arguments:
        
      url: the url of the website to scrape
      class: the class of the div element that contains the article
    You can run the script by running the command

python Web_scrape.py

You can also change the url and class variable to suit your scraping needs.

Please make sure that the paths you provide for the image_directory and table variables exist and are accessible.
Note

Scraping website's content without permission may be illegal and could result in legal action, so please make sure you have permission from the website owner before scraping their content.

Summary:
This is a python script that uses Selenium and Beautiful Soup to scrape articles from any website, it save the articles to a MySQL database, saves the images to a local folder, and saves the title, article and date to a local file. The user need to install the required software, packages and should change the path of the browser to match the path of geckodriver.exe file on their machine, update the host, user, password and the name of the database in the script and also update the path for the images and article.txt file.
