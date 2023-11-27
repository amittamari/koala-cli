#!/usr/bin/env python3

import typer

import install
import update
import lockfile

app = typer.Typer(name='koala-cli', no_args_is_help=True)
app.add_typer(install.app, name='install')
app.add_typer(update.app, name='update')
app.add_typer(lockfile.app, name='lockfile')

if __name__ == '__main__':
    app()
