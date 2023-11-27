#!/usr/bin/env python3

import typer

app = typer.Typer(no_args_is_help=True)

@app.command()
def health():
    raise NotImplementedError

if __name__ == '__main__':
    app()
