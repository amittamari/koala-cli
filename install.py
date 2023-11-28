#!/usr/bin/env python3

import typer

app = typer.Typer(no_args_is_help=True, help='Install KoalaVim and dependencies')

@app.command()
def install():
    raise NotImplementedError

if __name__ == '__main__':
    app()
