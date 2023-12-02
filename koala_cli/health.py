import typer

app = typer.Typer(help="Check KoalaVim's health")

@app.callback()
def health():
    print('Sorry, not implemented yet')
    raise typer.Exit(code=1)

