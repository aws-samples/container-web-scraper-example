
import time
import datetime
import boto3
from botocore.errorfactory import ClientError
from selenium import webdriver

from selenium.webdriver.firefox.options import Options


options = Options()
options.headless = True

driver=webdriver.Firefox(options=options, executable_path='/opt/geckodriver')

print('start your scraping project')

