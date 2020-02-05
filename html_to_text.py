## This script extracts plaintext from an external html document 
#Outputs a BS object
import urllib.request
from bs4 import BeautifulSoup
import random



def html_to_text(url):
    #Pretty self explanatory, but is easier than remebering this syntax every time
    html = urllib.request.urlopen(url)
    return BeautifulSoup(html,features="html.parser").get_text()

