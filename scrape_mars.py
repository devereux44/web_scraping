def scrape():
    import pandas as pd
    from splinter import Browser
    from bs4 import BeautifulSoup

    import requests
    import json
    import pymongo

    url = 'https://mars.nasa.gov/news/'

    # Retrieve page with the requests module
    response_news = requests.get(url)

    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(response_news.text, 'lxml')

    result = soup.find('div', class_='slide')
    #print(results)


    #for result in results_news:
    news_title = result.find('div', class_='content_title').text
    news_body = result.find('div', class_='rollover_description_inner').text


    print(news_title)
    print(news_body)

    article = {
    
    'title': news_title,
    'body': news_body
    
        }

    #begin process to find featured mars image
    #set up splinter to navigate to chrome browser
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    #Navigate to URL and click to featured image
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    browser.click_link_by_partial_text('FULL IMAGE')

    #scrape url to find featured img url
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
        # Retrieve all elements that contain book information
    image_path = []
    results_img = soup.find_all('img', class_='fancybox-image')
    for image in results_img:
        image_path = image['src']
        print(image_path)

    #add base_url and image_path for full_image_url
    base_url = 'https://www.jpl.nasa.gov'
    featured_image_url = base_url+str(image_path)
    print(featured_image_url)

    featured_image_url = {'Featured Image': featured_image_url}

    #Begin Process to scrape Twitter for Mars weather data
    url = 'https://twitter.com/marswxreport?lang=en'

    # Retrieve page with the requests module
    response = requests.get(url)

    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(response.text, 'lxml')

    results_twitter = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
    mars_weather = results_twitter
    print(mars_weather)

    mars_weather = {'mars_weather': mars_weather}


    #Begin Process to Scrape Table from Mars facts
    url = 'https://space-facts.com/mars/'

    tables = pd.read_html(url)
    tables

    df = tables[0]
    df.columns = ['Description', 'Values']
    df.head()

    df.set_index('Description', inplace=True)
    df.head()

    html_table = df.to_html()
    html_table

    html_table.replace('\n', '')

    #begin process to scrape the images of the hemispheres
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    #Navigate to URL and click to featured image
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    results_img_link = soup.find_all('h3')

    link_names = []

    for link_name in results_img_link:
        
        link_name = soup.find('h3').text
        link_names.append(link_name)

        print(link_names)

        url_mars = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(url_mars)
        browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')

    #scrape url to find featured img url
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
        # Retrieve all elements that contain book information
    image_path_mars_CHE = []
    results_mars = soup.find_all('img', class_='wide-image')
    for image in results_mars:
        image_path_mars_CHE = image['src']
        print(image_path_mars_CHE)

    mars_base_url = 'https://astrogeology.usgs.gov'
    CHE_path = mars_base_url + str(image_path_mars_CHE)
    print(CHE_path)

    url_mars = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_mars)
    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')

    #scrape url to find featured img url
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
        # Retrieve all elements that contain book information
    image_path_mars_SHE = []
    results_mars = soup.find_all('img', class_='wide-image')
    for image in results_mars:
        image_path_mars_SHE = image['src']
        print(image_path_mars_SHE)

    mars_base_url = 'https://astrogeology.usgs.gov'
    SHE_path = mars_base_url + str(image_path_mars_SHE)
    print(SHE_path)

    url_mars = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_mars)
    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')

    #scrape url to find featured img url
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
        # Retrieve all elements that contain book information
    image_path_mars_SMHE = []
    results_mars = soup.find_all('img', class_='wide-image')
    for image in results_mars:
        image_path_mars_SMHE = image['src']
        print(image_path_mars_SMHE)

    mars_base_url = 'https://astrogeology.usgs.gov'
    SMHE_path = mars_base_url + str(image_path_mars_SMHE)
    print(SMHE_path)

    url_mars = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_mars)
    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')

    #scrape url to find featured img url
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
        # Retrieve all elements that contain book information
    image_path_mars_VMHE = []
    results_mars = soup.find_all('img', class_='wide-image')
    for image in results_mars:
        image_path_mars_VMHE = image['src']
        print(image_path_mars_VMHE)

    mars_base_url = 'https://astrogeology.usgs.gov'
    VMHE_path = mars_base_url + str(image_path_mars_VMHE)
    print(VMHE_path)

    hemisphere_image_urls = [
    
    {"title": "Valles_Marineris_Hemisphere", "img_url_1": VMHE_path},
    {"title": "Cerberus_Hemisphere", "img_url_2": CHE_path},
    {"title": "Schiaparelli_Hemisphere", "img_url_3": SHE_path},
    {"title": "Syrtis_Major_Hemisphere", "img_url_4": SMHE_path}    
    
        ]

    print(hemisphere_image_urls)

    mars_data = {
    
    'hemisphere_pictures': hemisphere_image_urls,
    'featured_image': featured_image_url,
    'article': article,
    'mars_weather': mars_weather    
    }

    return mars_data