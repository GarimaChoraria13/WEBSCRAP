#WEb SCRAPPING FROM PYTHON.ORG SITE

#IMPORTING LIBRARY FOR WEB SCRAPPING
import requests
from bs4 import BeautifulSoup

def latest_news():
    url = "https://www.python.org/"
    r = requests.get(url)
    
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        latest_articles = []

        for article in soup.select('.blog-widget li'):
            title = article.a.text.strip()
            latest_articles.append(title)

        return latest_articles

    else:
        print(f'Failed to retrieve data. Status code: {r.status_code}')
        return []

if __name__ == "__main__":
    python_articles = latest_news()

    if python_articles:
        output_filepath='python_article.txt'
 # making text file print
        with open(output_filepath,'w',encoding='utf-8') as file:
            file.write('News on site is:\n')
            print(f'output has written to{output_filepath}')
# putting index on article in text file
            for index, article in enumerate(python_articles, 1):
                file.write(f'{index}. {article}\n')
    else:
      print('Sorry, no news available.')


