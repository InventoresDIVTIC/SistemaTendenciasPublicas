from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Replace with the URL of the tweet you want to scrape
tweet_url = 'https://twitter.com/user/status/1234567890123456789'

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # You'll need to have the ChromeDriver executable in your PATH
driver.get(tweet_url)
time.sleep(5)  # Wait for the page to load

# Scroll down to load more replies
body = driver.find_element_by_tag_name('body')
for _ in range(3):  # Adjust the number of scrolls based on the number of replies you want to load
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)

# Get comments (replies)
comments = driver.find_elements_by_css_selector('.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-5f2r5o.r-1mi0q7o')
comment_texts = [comment.text for comment in comments]

# Print and write comments to a file
with open('txt/tweets_selenium.txt', 'a', encoding='utf-8') as file:
    for item in comment_texts:
        print(item)
        file.write(item + '\n')

# Close the browser window
driver.quit()
