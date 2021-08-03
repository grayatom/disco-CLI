from .config import USER_EMAIL
# USER_EMAIL = 'bhargav@hyperverge.co'
from .Map import MAP


def get_filter_list(filters):
    filter_list_for_api = [f'UserDetails.Email:{USER_EMAIL}']
    for _filter in filters:
        try:
            key, val = _filter.split('=')
            # val = int(val) if key in int_type_filters else val
            filter_list_for_api.append(f'{MAP[key]["qf"]}:{val}')
        except KeyError as e:
            print(f'InvalidFilter: {e}')
            return False
        except ValueError as e:
            print(f'InvalidFilterFormat: the accepted format is "A=B"')
            return False
    return filter_list_for_api


def get_field_str(attributes_str):
    try:
        if attributes_str is not None:
            attributes = attributes_str.split(',')
            items = list(map(lambda f: MAP[f]['qf'], attributes))
            res = ','.join(items)
            return res
        else:
            return
    except KeyError as e:
        print(f'InvalidFieldValue: {e}')
        return False