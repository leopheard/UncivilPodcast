import requests
import re
from bs4 import BeautifulSoup

def get_soup1(url1):
    page = requests.get(url1)
    soup1 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup1))
    return soup1

def get_playable_podcast1(soup1):
    subjects = []
    for content in soup1.find_all('item', limit=14):
        try:
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://images.megaphone.fm/NFdjH-wRQZZ8Ab1IKyz7seULZ5rL0kBw75srJmCAw7w/plain/s3://megaphone-prod/podcasts/60cff344-5135-11e7-a8cc-e3b7831c52a1/image/uploads_2F1558660601536-wozn3ad3hf-6d7f93b4725ebacce11efa05e6db5370_2F201905_Uncivil-ShowCover-Peabody.png",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast1(playable_podcast1):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast(soup1):
    subjects = []
    for content in soup1.find_all('item'):
        try:
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://images.megaphone.fm/NFdjH-wRQZZ8Ab1IKyz7seULZ5rL0kBw75srJmCAw7w/plain/s3://megaphone-prod/podcasts/60cff344-5135-11e7-a8cc-e3b7831c52a1/image/uploads_2F1558660601536-wozn3ad3hf-6d7f93b4725ebacce11efa05e6db5370_2F201905_Uncivil-ShowCover-Peabody.png",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast(playable_podcast):
    items = []
    for podcast in playable_podcast:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items
