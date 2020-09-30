# DTAC (Docopt Trello API CLI)
```
Trello CLI.

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

## To add a card with labels on board Y to the X column with labels and a comment:
- fetch all boards and explore ids - `member-boards`
- fetch all lists for a board - `boards <board-id> lists`
- fetch all labels for a board - `boards <board-id> labels`
- create a card on a list - `cards --create='{"name": <card-name>, "idList":<list-id>, "idLabels":[<label-id-1>, <label-id-2>]}'`
- add a comment to the card - `cards <card-id> comments --create='{"text": <comment-text>}'`
