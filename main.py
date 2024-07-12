import time
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def Script(index):
    driver = webdriver.Chrome()
    driver.get("https://onemillioncheckboxes.com/")
    time.sleep(10)
    while True:
        checkbox = driver.find_element(By.ID, f"checkbox-{index}")
        if checkbox.is_selected():
            checkbox.click()
            print(index)
            time.sleep(0.1)
    driver.close()

if __name__ == "__main__":
    number_threads = int(input("Number of threads: "))
    number_of_running_threads = 0
    while number_of_running_threads != number_threads:
        print(f"Starting Thread: {number_of_running_threads + 1}")
        thread = threading.Thread(target=Script, args=(number_of_running_threads,))
        thread.start()
        number_of_running_threads += 1