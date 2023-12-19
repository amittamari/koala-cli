import typer

app = typer.Typer(help='Updata KoalaVim and dependencies')


@app.callback(invoke_without_command=True)
def update():
    print('Sorry, not implemented yet')
    raise typer.Exit(code=1)
