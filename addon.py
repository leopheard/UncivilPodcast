from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://feeds.megaphone.fm/uncivil"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://images.megaphone.fm/NFdjH-wRQZZ8Ab1IKyz7seULZ5rL0kBw75srJmCAw7w/plain/s3://megaphone-prod/podcasts/60cff344-5135-11e7-a8cc-e3b7831c52a1/image/uploads_2F1558660601536-wozn3ad3hf-6d7f93b4725ebacce11efa05e6db5370_2F201905_Uncivil-ShowCover-Peabody.png"},
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://images.megaphone.fm/NFdjH-wRQZZ8Ab1IKyz7seULZ5rL0kBw75srJmCAw7w/plain/s3://megaphone-prod/podcasts/60cff344-5135-11e7-a8cc-e3b7831c52a1/image/uploads_2F1558660601536-wozn3ad3hf-6d7f93b4725ebacce11efa05e6db5370_2F201905_Uncivil-ShowCover-Peabody.png"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes/')
def episodes():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

if __name__ == '__main__':
    plugin.run()
