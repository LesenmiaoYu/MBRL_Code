from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
from PyPDF2 import PdfReader
import os

# Automatically set up the WebDriver with ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the Sci-Hub website once to bypass DDOS guard
driver.get("https://sci-hub.se")
time.sleep(30)  # Allow time to bypass any manual checks

# Function to search Sci-Hub and check for keyword in the PDF
def search_and_check_keyword(row, keyword):
    try:
        title = row['Title']

        # Click the logo to return to the main page after each process
        logo_element = driver.find_element(By.ID, "header")

        # Refresh the page instead of opening a new one
        time.sleep(5)  # Allow time for the page to reload

        # Search for the title
        search_box = driver.find_element(By.ID, "request")
        search_box.clear()  # Clear the search box
        search_box.send_keys(title)
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)  # Allow time for the page to load

        # Check if the "document not found" message is displayed
        if "Sci-Hub doesn't have the requested document" in driver.page_source:
            print(f"Document not found for title: {title}. Clicking 'Return to main page'...")
            try:
                return_main_page = driver.find_element(By.ID, "return")
                return_main_page.click()
                time.sleep(5)  # Allow time to navigate back
            except Exception as e:
                print(f"Error clicking 'Return to main page': {e}")
            return "Not Found"

        # Check if PDF viewer is present
        save_button = driver.find_element(By.TAG_NAME, 'button')

        if save_button:
            save_button.click()  # Click the save button to download the PDF
            time.sleep(5)  # Allow time for the download
            print(f"PDF saved for title: {title}")
            time.sleep(2)

            # Click the logo to return to the main page
            logo_element.click()
            time.sleep(5)
            return "Saved"


        # Click the logo to return to the main page after processing
        time.sleep(5)
        return "No"

    except Exception as e:
        print(f"Error processing title '{row['Title']}': {e}")
        return "Error"

# Load dataset
input_file = "paper_screening_results.csv"  # Replace with your input file path
data = pd.read_csv(input_file)

# Add a new column for keyword presence
keyword = "University of Southern California"  # Replace with your desired keyword
data["Keyword_Present"] = data.apply(lambda row: search_and_check_keyword(row, keyword), axis=1)

# Save updated dataset
data.to_csv("scanned_results.csv", index=False)

# Close the browser
time.sleep(10)  # Wait for 10 seconds before closing the browser
driver.quit()
