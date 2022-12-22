JUST:="just --justfile="+justfile()

@_all:
    {{ JUST }} --list

run:
    {{ JUST }} example flask-app


pytest NAME='tests/':
    poetry run pytest {{ NAME }}

example NAME:
    PYTHONPATH={{ justfile_directory() }} poetry run python examples/{{ NAME }}.py

pwd: 
    poetry run echo 




