__author__ = 'kic'
from forum_app.settings import prefix_url

user_urls = {'user_create': prefix_url + 'user/create/',
             'user_listPosts': prefix_url + 'user/listPosts/',
             'user_details': prefix_url + 'user/details/',
             'user_follow': prefix_url + 'user/follow/',
             'user_update': prefix_url + 'user/updateProfile/',
             'user_unfollow': prefix_url + 'user/unfollow/'}
