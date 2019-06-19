from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
import time;

driver = webdriver.Firefox();
driver.get("https://www.python.org");

elem = driver.find_element_by_name("q");
elem.clear();
elem.send_keys("pycon");
time.sleep(3);
elem.send_keys(Keys.RETURN);
time.sleep(3);

driver.close()
