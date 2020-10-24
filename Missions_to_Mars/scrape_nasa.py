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

    #imports url
    html = browser.html
    soup = bs(html, 'html.parser')  
    slide_el = soup.select_one("ul.item_list li.slide")

    #find and print title
    news_title = slide_el.find("div", class_="content_title").get_text()
    print(news_title)

    #find and print body
    news_p=slide_el.find("div", class_="article_teaser_body").get_text()
    print (news_p)

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    #find the image background url

    html = browser.html
    soup = bs(html, 'html.parser')  

    #first click Full-image to go to full image page
    browser.links.find_by_partial_text('FULL').click()

    browser.links.find_by_partial_text('more info').click()

    #now we are in full image link, find the URL Image
    html = browser.html
    soup = bs(html, 'html.parser') 

    time.sleep(5)

    imgs =  soup.find("figure", class_= "lede")
    # print(imgs)

    links_with_text = [a['href'] for a in imgs.find_all('a', href=True)]
    # elements = imgs.find_by_tag('a')
    print(links_with_text)

    nasa_image = "https://www.jpl.nasa.gov" + links_with_text[0] 

    # # Store data in a dictionary
    nasa_data = {
        "news_title": news_title,
        "news_p": news_p,
        "nasa_image": nasa_image
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return nasa_data
