from bs4 import BeautifulSoup
import requests

list_actor_history = []
try:
    def connect_html(link):
        global soup
        source = requests.get(link)
        source.raise_for_status()
        soup = BeautifulSoup(source.text,'html.parser') # what does the parser do
    connect_html('https://www.imdb.com/title/tt0110912/?ref_=nv_sr_srsg_0')
    actors = soup.find('div', class_="ipc-sub-grid ipc-sub-grid--page-span-2 ipc-sub-grid--wraps-at-above-l ipc-shoveler__grid").find_all('div', class_="sc-bfec09a1-5 dGCmsL")
    for actor in actors:
        list_move_name = []
        name = actor.find('div', class_='sc-bfec09a1-7 iDmJtd').a
        actor_history = {'name':name.text,'link':f"https://www.imdb.com{name.get('href')}"}
        connect_html(f"https://www.imdb.com{name.get('href')}")
        movies = soup.find('div', class_='filmo-category-section').find_all('div', class_='filmo-row')
        for movie in movies:
            movie_name = movie.find('b').a
            list_move_name.append(movie_name.text)
        actor_history['movies'] = list_move_name
        list_actor_history.append(actor_history)
        print('done')

except Exception as e:
    print(e)

print(list_actor_history)