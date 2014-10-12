__author__ = 'kic'
import copy

from forum_app.api_packs.forum_api.forum_consts import forum_create_response


def get_forum_response(fid, name, short_name, user, code=0):
    response = copy.deepcopy(forum_create_response)

    response['code'] = code
    response['response']['id'] = fid
    response['response']['name'] = name
    response['response']['short_name'] = short_name
    response['response']['user'] = user

    return response