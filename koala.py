#!/usr/bin/env python3

from os import mkdir

import install
import lockfile
import update
import health
from utils import data_dir

import typer

app = typer.Typer(name='koala-cli', no_args_is_help=True, help='CLI tool to manage KoalaVim')
app.add_typer(install.app, name='install')
app.add_typer(update.app, name='update')
app.add_typer(lockfile.app, name='lockfile')
app.add_typer(health.app, name='health')

def init():
    try:
        mkdir(data_dir())
    except FileExistsError:
        pass

if __name__ == '__main__':
    init()
    app()
