__author__ = 'kic'
from forum_app.api_packs.user_api.user_details import get_details_user


def get_user_list_followers(data):
    code = 0

    user_info = get_details_user(data)['response']
    user_code = get_details_user(data)['code']

    since = data.get('since_id', [0, ])[0]
    limit = data.get('limit', [0, ])[0]
    is_desc = 0
    order_by = data.get('order', ['asc', ])
    if 'desc' in order_by:
        is_desc = 1

    followers_list = []
    filter2 = []

    if user_code == 0:
        for x in user_info['followers']:
            usr_details = get_details_user({'user': [x, ]})
            usr_details = usr_details['response']
            followers_list.append(usr_details)

        filter1 = [x for x in followers_list if x['id'] >= int(since)]
        filter2 = sorted(filter1, key=lambda a: a['name'], reverse=is_desc)

        if limit:
            filter2 = filter2[0:int(limit)]
    else:
        code = user_code

    res_dict = {'code': code, 'response': filter2}
    return res_dict