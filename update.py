#!/usr/bin/env python3

import typer

app = typer.Typer(no_args_is_help=True, help='Updata KoalaVim and dependencies')

@app.command()
def update():
    raise NotImplementedError

if __name__ == '__main__':
    app()
