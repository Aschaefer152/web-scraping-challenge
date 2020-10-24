from splinter import Browser
from bs4 import BeautifulSoup as bs
import time



def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit 
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
   

    # Get the average temps
    news_title = soup.find("div", class_="content_title").get_text()

    time.sleep(1)
    # # Get the min avg temp
    # min_temp = avg_temps.find_all('strong')[0].text

    # # Get the max avg temp
    # max_temp = avg_temps.find_all('strong')[1].text

    # # BONUS: Find the src for the sloth image
    # relative_image_path = soup.find_all('img')[2]["src"]
    # sloth_img = url + relative_image_path

    # # Store data in a dictionary
    nasa_data = {
        "news_title": news_title
    #     "min_temp": min_temp,
    #     "max_temp": max_temp
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return nasa_data
