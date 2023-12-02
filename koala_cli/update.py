import typer

app = typer.Typer(help='Updata KoalaVim and dependencies')

@app.callback()
def update():
    print('Sorry, not implemented yet')
    raise typer.Exit(code=1)
