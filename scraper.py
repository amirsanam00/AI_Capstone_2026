from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def get_constitution_text():
    options = Options()
    options.add_argument("--headless")
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://leginfo.legislature.ca.gov/faces/codesTOCSelected.xhtml?tocCode=CONS")
    time.sleep(3)
    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    
    return soup.get_text()

if __name__ == "__main__":
    text = get_constitution_text()
    with open("constitution.txt", "w") as f:
        f.write(text)
    print("California Constitution saved!")