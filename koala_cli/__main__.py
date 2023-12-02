import typer

from koala_cli import install, update, lockfile, health

app = typer.Typer(name='koala', no_args_is_help=True, help='CLI tool to manage KoalaVim')
app.add_typer(install.app, name='install', invoke_without_command=True)
app.add_typer(update.app, name='update', invoke_without_command=True)
app.add_typer(lockfile.app, name='lockfile')
app.add_typer(health.app, name='health', invoke_without_command=True)

if __name__ == '__main__':
    app(prog_name='koala-cli')
