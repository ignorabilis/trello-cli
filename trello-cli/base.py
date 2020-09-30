"""Trello CLI.

Usage:
  base.py member-boards
  base.py boards [--create=<data>]
  base.py boards <id>
  base.py boards <id> [--delete | --update=<data>]
  base.py boards <id> [<nested-entity>]
  base.py (-h | --help)
  base.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
from __init__ import __version__
import json
from docopt import docopt
import requests

TRELLO_KEY = '65217e4e50a903965f736c3111ca0aa0'
TRELLO_TOKEN = 'b585a86b71fb937dcd873ebe0d63e1754028ac0020a6ad966ea91209128de019'
TRELLO_URL = 'https://api.trello.com/1/'
NAMED_COMMANDS = {'member-boards': 'members/me/boards'}


def get_http_method(arguments):
    if arguments['--create']:
        return ['POST', arguments['--create']]
    elif arguments['--update']:
        return ['PUT', arguments['--update']]
    elif arguments['--delete']:
        return ['DELETE', None]
    else:
        return ['GET', None]


def get_trello_command(arguments):
    # simple iteration
    for key, value in arguments.items():
        if not key.startswith('--') and not key.startswith('<') and value:
            return NAMED_COMMANDS.get(key, None) or key

    # functional alternative
    # command = next(filter(lambda key: not key.startswith('--')
    #                       and not key.startswith('<') and arguments[key],
    #                       arguments), None)
    # return NAMED_COMMANDS.get(command, None) or command


def handle_arguments(arguments):
    request_method, request_body = get_http_method(arguments)
    command = get_trello_command(arguments)
    id_arg = arguments['<id>']
    nested_entity_arg = arguments['<nested-entity>']
    final_url = TRELLO_URL + command + ('/' + id_arg if id_arg else '') + ('/' + nested_entity_arg if nested_entity_arg else '')
    json_body = json.loads(request_body) if request_body else None

    # uncomment for debugging
    # print(request_method, command, id_arg, final_url, json_body)

    response = requests.request(
        request_method,
        final_url,
        json=json_body,
        params={'key': TRELLO_KEY, 'token': TRELLO_TOKEN})

    # uncomment for debugging
    # print(response)
    print(response.json())


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Trello CLI ' + __version__)
    handle_arguments(arguments)
