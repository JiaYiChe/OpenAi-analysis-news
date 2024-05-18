import requests
from bs4 import BeautifulSoup
import openai
import os
import datetime
import webbrowser

# set the API key
openai.api_key = 'Your API key here'

# website URL
url = 'your website URL here'

# send HTTP request to the website
response = requests.get(url)

def get_chatgpt_response(news, model="gpt-3.5-turbo", max_tokens=1000):
    
    response = openai.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": news}],
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response.choices[0].message['content']

def web_show(analysed):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    html_filename = f"info_{timestamp}.html"
    with open(html_filename, "w") as f:
        f.write(analysed)
    webbrowser.open("analysed.html")

def main():
    # check if the request is successful
    if response.status_code == 200:
        # use BeautifulSoup to parse the website
        soup = BeautifulSoup(response.text, 'html.parser')
        news_items = soup.find_all()  # find all news items, in the brackets you can specify the tag you want to search for

        news = ""
        #title can be changed to the tag you want to search for
        for title in news_items:
            if title.text:
                news += title.text
            else:
                break
    else:
        print('Failed to retrieve data')
    
    analysed = get_chatgpt_response(news)


if __name__ == "__main__":
    main()