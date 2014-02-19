"""
    From the list of shows in the request payload, return the ones with DRM enabled (drm: true) and at least one episode (episodeCount > 0).

    The returned JSON should have a response key with an array of shows. Each element should have the following fields from the request:

    image - corresponding to image/showImage from the request payload
    slug
    title

    If we send invalid JSON, You'll need to return a JSON response with HTTP status 400 Bad Request,
    and with a `error` key containing the string Could not decode request.

"""
import json
import sys


def filter_json_request(json_object):
    try:
        # matching_shows = filter(_is_matching_show, json_object['payload'])
        # mapped_shows = map(_pick_fields, matching_shows)
        # return {'response': mapped_shows}

        # Or we can just use a list comprehension for map/filter
        return {'response': [_pick_fields(show) for show in json_object['payload'] if _is_matching_show(show)] }
    except (KeyError, TypeError, ValueError) as e:
        raise BadJsonException(str(e)), None, sys.exc_info()[2]


def _is_matching_show(show):
    try:
        drm = bool(show['drm'])
        episode_count = int(show['episodeCount'])
        return drm and episode_count > 0
    except (KeyError, TypeError, ValueError):
        return False


def _pick_fields(show):
    return dict(image=show['image']['showImage'], slug=show['slug'], title=show['title'])


def filter_string_request(json_string):
    try:
        json_request = json.loads(json_string)
    except ValueError as e:
        raise BadJsonException(str(e)), None, sys.exc_info()[2]
    else:
        return filter_json_request(json_request)


class BadJsonException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
