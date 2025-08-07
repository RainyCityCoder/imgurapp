'''
Author: RainyCityCoder
Description: Script to speed upload of images to Imgur
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass


def signin(imgur_driver, username, password):
    '''
    Handles signin
    
    Args:
        imgur_driver (Driver object): Firefox session
        username (str): user-input Imgur username
        password (str): user-input Imgur password
        
    Return: None
    '''

    imgur_signin_url = "https://imgur.com/signin#%2F"
    
    try:
        imgur_driver.get(imgur_signin_url)
        try:
            WebDriverWait(imgur_driver, 20).until(EC.element_to_be_clickable((
                By.NAME, "username")))
        except: print("input fields not found")
        imgur_driver.find_element(By.NAME, "username").send_keys(username)
        imgur_driver.find_element(By.NAME, "password").send_keys(password)
        imgur_driver.find_element(By.NAME, "submit").click()
    except Exception as ex:
        print("Error: "+str(ex))
    print("Sign-in successful")
        
        
def upload(imgur_driver):
    '''
    Uploads photo
    
    Args:
        imgur_driver ():
        
    Return: None
    '''

    upload_url = "https://imgur.com/upload"
    print("Attempting to ping imgur upload url")
    
    try:
        WebDriverWait(imgur_driver, 20).until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "UploadSpinner-contentWrapper")))
        imgur_driver.get(upload_url)
        print("successfully utilized imgur.com/upload")
    except: print("Couldn't utilize imgur.com/upload")
    
    print("Attempting to click file upload button")
    try:
        WebDriverWait(imgur_driver, 20).until(EC.element_to_be_clickable((
            By.CLASS_NAME, "PopUpActions-filePicker"))).click()
        print("Was able to click on file upload button")   
    except: print("couldn't click on upload file button")
                                  
    
def main():
    '''
    Main program flow, calls specific functions in sequence.
    
    Args: None
    
    Return: None
    '''
    
    username = input("Please enter your username: ")
    password = getpass("Please enter your password: ")
    imgur_driver = webdriver.Firefox()
    
    try:
        print("Calling sign-in function.")
        signin(imgur_driver, username, password)
    except Exception as ex:
        print("Sign-in Error: "+str(ex))
        
    try:
        print("Calling upload function")
        upload(imgur_driver, username)
    except Exception as ex:
        print("Upload Error: "+str(ex))
        
    
if __name__ == '__main__':
    main()  