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


def filter_json_request(json_object):
    try:
        payload = json_object['payload']
        matching_shows = filter(_is_matching_show, payload)
        mapped_shows = map(_pick_fields, matching_shows)
        response = {'response': mapped_shows}
        return response
    except (KeyError, TypeError, ValueError):
        return build_error_object()


def _is_matching_show(show):
    try:
        drm = bool(show['drm'])
        episode_count = int(show['episodeCount'])
        return drm and episode_count > 0
    except (KeyError, TypeError, ValueError):
        return False


def _pick_fields(show):
    return dict(image=show['image']['showImage'], slug=show['slug'], title=show['title'])


def build_error_object():
    return {"error": "Could not decode request"}
    # return json.loads('{"error": "Could not decode request"}')


def filter_string_request(json_string):
    try:
        json_request = json.loads(json_string)
        return filter_json_request(json_request)
    except ValueError:
        # invalid JSON in the request
        return build_error_object()
