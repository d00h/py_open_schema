JUST:="just --justfile="+justfile()

@_all:
    {{ JUST }} --list


pytest NAME='tests/':
    poetry run pytest {{ NAME }}


example NAME:
    poetry run python examples/{{ NAME }}.py


