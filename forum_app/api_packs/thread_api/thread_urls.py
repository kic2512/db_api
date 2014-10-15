__author__ = 'kic'
from forum_app.settings import prefix_url

thread_urls = {'thread_create': prefix_url + 'thread/create/',
               'thread_close': prefix_url + 'thread/close/',
               'thread_remove': prefix_url + 'thread/remove/',
               'thread_open': prefix_url + 'thread/open/'}
