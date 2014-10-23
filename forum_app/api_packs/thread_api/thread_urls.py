__author__ = 'kic'
from forum_app.settings import prefix_url

thread_urls = {'thread_create': prefix_url + 'thread/create/',
               'thread_close': prefix_url + 'thread/close/',
               'thread_remove': prefix_url + 'thread/remove/',
               'thread_open': prefix_url + 'thread/open/',
               'thread_details': prefix_url + 'thread/details/',
               'thread_restore': prefix_url + 'thread/restore/',
               'thread_update': prefix_url + 'thread/update/',
               'thread_listPosts': prefix_url + 'thread/listPosts/',
               'thread_list': prefix_url + 'thread/list/',
               'thread_vote': prefix_url + 'thread/vote/',
               'thread_subscribe': prefix_url + 'thread/subscribe/',
               'thread_unsubscribe': prefix_url + 'thread/unsubscribe/',
               }
