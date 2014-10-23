__author__ = 'kic'

from forum_app.settings import prefix_url

forum_urls = {'forum_create': prefix_url + 'forum/create/',
              'forum_listUsers': prefix_url + 'forum/listUsers/',
              'forum_listPosts': prefix_url + 'forum/listPosts/',
              'forum_listThreads': prefix_url + 'forum/listThreads/',
              'forum_details': prefix_url + 'forum/details/'}

