import requests
from llama import create_summary
from bs4 import BeautifulSoup
import datetime


def get_url(id):
    return (f"https://hacker-news.firebaseio.com/v0/item/{id}.json")


# prepares the html content for the newsletter
def newsletter_html(data, n, body_template="body_template.html", block_template="block_template.html"):
    # prepares soup for body_template
    with open(body_template, 'r', encoding='utf-8') as file:
        body_soup = BeautifulSoup(file, 'html.parser')
    body = body_soup.find('div', class_='container')

    # iterate through the data list
    for i in range (0, n):
        id = data[i]
        response = requests.get(get_url(id))

        # extract info
        if response.status_code != 200 :
            raise ValueError("Article not accessible with given id. Check if article exists")
        object = response.json()
        title = object.get("title")
        url = object.get("url")
        summary = create_summary(url)

        # prepare soup for block elements
        with open(block_template, 'r', encoding='utf-8') as file:
            block_soup = BeautifulSoup(file, 'html.parser')
        title_tag = block_soup.find('div', class_='title').find('a')
        summary_tag = block_soup.find('div', class_='summary')
        title_tag.string = title
        title_tag['href'] = url
        summary_tag.string = summary + "..."

        body.append(block_soup.div)


    date = datetime.date.today()
    body_soup.find(id='currentDate').string = str(date)

    # return the modified HTML as a string
    return str(body_soup)









