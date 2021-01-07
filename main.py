import requests
from bs4 import BeautifulSoup


# определяем список ключевых слов
KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'марафон']
response = requests.get('https://habr.com/ru/all/')
soup = BeautifulSoup(response.text, 'html.parser')
posts = soup.find_all('article', class_='post')
for post in posts:
    hubs = post.find_all('div', class_='post__text-html')
    hubs_text = list(map(lambda x: x.text.strip().lower(), hubs))
    dt = post.find('span', class_='post__time').text
    link = post.find('a', class_='post__title_link')
    link_link = link.attrs.get('href')
    link_text = link.text.strip()
    for hub_text in hubs_text:
        if any((word in hub_text for word in KEYWORDS)):
            print(dt, link_text, link_link)
            #print('preview')
            break
        else:
            response_post = requests.get(link_link)
            soup_post = BeautifulSoup(response_post.text, 'html.parser')
            texts = soup_post.find_all('div', id='post-content-body')
            text = list(map(lambda x: x.text.strip().lower(), texts))
            if any((word in text[0] for word in KEYWORDS)):
                print(dt, '-', link_text, '-', link_link)
                #print('full_text')
                break
