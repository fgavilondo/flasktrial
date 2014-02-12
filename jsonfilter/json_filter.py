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


def _is_matching_show(show):
    try:
        drm = bool(show['drm'])
        episode_count = int(show['episodeCount'])
        return drm and episode_count > 0
    except (KeyError, TypeError, ValueError):
        return False


def _pick_fields(show):
    return dict(image=show['image']['showImage'], slug=show['slug'], title=show['title'])


def filter_request_from_string_return_object(json_string):
    try:
        request = json.loads(json_string)
    except ValueError:
        # invalid JSON in the request
        return json.loads('{"error": "Could not decode request"}')
    else:
        payload = request['payload']
        matching_shows = filter(_is_matching_show, payload)
        mapped_shows = map(_pick_fields, matching_shows)
        response = {'response': mapped_shows}
        return response


def filter_request_from_string_return_string(json_string):
    json_object = filter_request_from_string_return_object(json_string)
    return json.dumps(json_object)


def filter_request_from_file_return_object(json_file_name):
    with open(json_file_name, "r") as f:
        json_string = f.read()
        return filter_request_from_string_return_object(json_string)


def filter_request_from_file_return_string(json_file_name):
    with open(json_file_name, "r") as f:
        json_string = f.read()
        return filter_request_from_string_return_string(json_string)


if __name__ == "__main__":
    import sys

    print filter_request_from_file_return_string(sys.argv[1])


