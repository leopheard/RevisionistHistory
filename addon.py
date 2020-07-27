from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://feeds.megaphone.fm/revisionisthistory"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://images.megaphone.fm/pQuVxKWxL-LOGpSHlp8QYL792qunwAqhdcLR6S7ERTU/plain/s3://megaphone-prod/podcasts/1427a2f4-2674-11e6-a3d7-cf7ee2a2c03c/image/uploads_2F1592404340573-bgxnavis74n-2a4c211c2dce427220c794dcbef06962_2FRH%2BFinal%2BArtwork%2BPushkin.jpg"},
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://images.megaphone.fm/pQuVxKWxL-LOGpSHlp8QYL792qunwAqhdcLR6S7ERTU/plain/s3://megaphone-prod/podcasts/1427a2f4-2674-11e6-a3d7-cf7ee2a2c03c/image/uploads_2F1592404340573-bgxnavis74n-2a4c211c2dce427220c794dcbef06962_2FRH%2BFinal%2BArtwork%2BPushkin.jpg"},
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
