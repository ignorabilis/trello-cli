# DTAC (Docopt Trello API CLI)
```
DTAC (Docopt Trello API CLI)

Usage:
  base.py member-boards
  base.py boards [--create=<data>]
  base.py boards <id>
  base.py boards <id> [--delete | --update=<data>]
  base.py boards <id> [<nested-entity>]
  base.py cards [--create=<data>]
  base.py cards <id>
  base.py cards <id> [--delete | --update=<data>]
  base.py cards <id> [<nested-entity> --create=<data>]
  base.py (-h | --help)
  base.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.

```
## Credentials
To access the Trello API you will need a key and a token - for more info on generating these check Trello's [Developer API Keys](https://trello.com/app-key). The CLI expects two environment variables, `TRELLO_KEY` & `TRELLO_TOKEN`- if not set a message will be displayed.

## To add a card with labels on board Y to the X column with labels and a comment:
- cd into source folder and install requirements - `pip install -r requirements.txt`
- all of the following commands should be preceded by `python trello-cli/base.py`
- fetch all boards and explore ids - `member-boards`
- fetch all of the lists on a board (and find id) - `boards <board-id> lists`
- fetch all of the labels on a board (and find ids) - `boards <board-id> labels`
- create a card on a list - `cards --create='{"name": <card-name>, "idList":<list-id>, "idLabels":[<label-id-1>, <label-id-2>]}'`
- add a comment to the card - `cards <card-id> comments --create='{"text": <comment-text>}'`

## Future development
- find how to refresh the Trello token (it has been exposed in this repo in previous commits)
- explore the whole Trello API
- explore if the current CLI format is good enough
- explore ways to improve the docopt help message - [this](https://github.com/docopt/docopt/tree/master/examples) and [this](https://github.com/docopt/docopt/tree/master/examples/git)
- ideally new request types & endpoints can be implemented by only changing the docopt help message - the current challenge is to find a better way to handle paths like `/members/me/boards` & `/actions/comments`
- expose Trello's key and token config as docopt options and fallback to environment variables
- add proper nested entities support - currently any value is allowed for a nested entity, but these should be restricted depending on the command
- make the CLI installable
- choose a test framework and start adding tests
- single source of truth - read the docopt help message from this readme - that way a change here would be reflected directly in the code!
- implement the whole Trello API
- logging + verbose options
- custom colors, formatting, others
