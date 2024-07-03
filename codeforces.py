import requests
from bs4 import BeautifulSoup as bs
import re

temp = []

def removeTags(text):
    return re.sub(r'<[^>]*>', '', text)

def cfRating(username):
    print("Fetching Codeforces Profile....")
    profile = 'https://codeforces.com/profile/'+username
    req = requests.get(profile)
    soup = bs(req.text,'html.parser')
    temp = soup.find_all('span',class_='user-gray')

    print("+--------------------+")
    print("| CodeForces Profile |")
    print("+--------------------+")
    print("Profile Link :",profile)
    print("UserName :",username)
    print("Present Title: "+removeTags(str(temp[0])))
    print("Maximum Title: "+removeTags(str(temp[-2])))
    print("Present Rating: "+removeTags(str(temp[1])))
    print("Maximum Rating: "+removeTags(str(temp[-1])))

cfRating('KLU_2100030053')