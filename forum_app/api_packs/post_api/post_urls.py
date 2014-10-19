__author__ = 'kic'
from forum_app.settings import prefix_url

post_urls = {'post_create': prefix_url + 'post/create/',
             'post_remove': prefix_url + 'post/remove/',
             'post_restore': prefix_url + 'post/restore/',
             'post_update': prefix_url + 'post/update/',
             'post_vote': prefix_url + 'post/vote/',
             'post_list': prefix_url + 'post/list/',
             'post_details': prefix_url + 'post/details/'}