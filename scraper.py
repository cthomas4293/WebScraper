import requests  # allows us to download HTML from website
from bs4 import BeautifulSoup  # allows us to grab HTML data, parse  it and manipulate it for use
# helps with printing to the terminal
import pprint

# Doing a get request to grab the html file from the web server
response = requests.get('https://news.ycombinator.com/news')
response2 = requests.get('https://news.ycombinator.com/news?p=2')
# create bs4 object to parse through request data
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

soup2 = BeautifulSoup(response.text, 'html.parser')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_link = links + links2
mega_subtext = subtext + subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['vote'], reverse=True)


def create_custom_hn(lnk, st):
    hn = []
    for idx, item in enumerate(lnk):
        title = item.getText()
        href = item.get('href', None)
        vote = st[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(" points", ''))
            if points > 99:
                hn.append(dict(title=title, link=href, vote=points))
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mega_link, mega_subtext))
