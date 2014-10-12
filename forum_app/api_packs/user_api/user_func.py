__author__ = 'kic'
import copy

from forum_app.api_packs.user_api.user_consts import user_create_response


def get_user_response(uid, username, about, name, email, isanonymous=0, code=0):
    response = copy.deepcopy(user_create_response)

    response['code'] = code
    response['response']['id'] = uid
    response['response']['name'] = name
    response['response']['username'] = username
    response['response']['email'] = email
    response['response']['isAnonymous'] = isanonymous
    response['response']['about'] = about

    return response
