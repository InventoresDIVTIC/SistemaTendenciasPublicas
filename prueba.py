from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.keys import Keys
import time

# Create a new instance of the Edge driver using webdriver_manager
driver = webdriver.Edge(EdgeChromiumDriverManager().install())

# Open Twitter login page
driver.get("https://twitter.com/login")

# Wait for the page to load
time.sleep(2)

# Fill in the login credentials
username = "alejandraroobles3@gmail.com"
password = "Ale123roblesmora"

# Find the username and password input fields and fill them
username_field = driver.find_element_by_name("session[username_or_email]")
password_field = driver.find_element_by_name("session[password]")

username_field.send_keys(username)
password_field.send_keys(password)

# Submit the login form
password_field.send_keys(Keys.RETURN)

# Wait for the login to complete (you might need to adjust the time)
time.sleep(5)

# Now you can interact with the Twitter page as needed
# For example, you can post a tweet or perform other actions

# Close the browser window
driver.quit()
