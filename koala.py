#!/usr/bin/env python3

import typer

import install
import update
import lockfile
import health

app = typer.Typer(name='koala-cli', no_args_is_help=True, help='CLI tool to manage KoalaVim')
app.add_typer(install.app, name='install')
app.add_typer(update.app, name='update')
app.add_typer(lockfile.app, name='lockfile')
app.add_typer(health.app, name='health')

if __name__ == '__main__':
    app()
