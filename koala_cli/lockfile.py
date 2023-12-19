import typer
import json
from typing_extensions import Annotated
from pathlib import Path

from rich.console import Console
from rich.table import Table
from rich.prompt import Confirm
from rich.style import Style

from koala_cli.utils import kvim_dir, config_dir

app = typer.Typer(no_args_is_help=True, help="Manage plugin's lockfile")


@app.command()
def diff():
    """
    Show differences of user lock-file from Koala's lock-file
    """
    kvim_lockfile = read_lockfile(kvim_dir())
    user_lockfile = read_lockfile(config_dir())

    table = Table(title='Lock File Diff')
    table.add_column('Name', style='medium_purple3')
    table.add_column('User', style='green')
    table.add_column('KoalaVim', style="cyan")

    for plugin, kvim_commit in kvim_lockfile.items():
        if plugin == 'KoalaVim':
            continue # The user can't never be in the correct commit
        user_commit = user_lockfile.get(plugin, "[grey35]N/A")
        if kvim_commit != user_commit:
            table.add_row(plugin, user_commit, kvim_commit)

    console = Console()
    console.print(table)

Yes = Annotated[bool, typer.Option("--yes", "-y", help="Don't ask for confirmation")]

@app.command()
def overwrite(yes: Yes = False):
    """
    Overwrite user lock-file with Koala's lockfile
    """
    _overwrite_lock_file(kvim_lockfile(), user_lockfile(), yes)

    console = Console()
    console.print("")
    console.print(" >> Run `:Lazy restore` in order to sync plugins to the lock file", style=Style(color="bright_yellow", bold=True))

@app.command()
def set_koalavim(yes: Yes = False):
    """
    Overwrite Koala's lock-file with user lockfile (used by devs)
    """
    _overwrite_lock_file(user_lockfile(), kvim_lockfile(), yes)

def _overwrite_lock_file(src, dst, yes=False):
    if not yes and not Confirm.ask(f"Confirm overwrite of '{dst}'"):
        return

    with open(src, 'r') as f:
        content: dict = json.load(f)
        content.pop("KoalaVim", None) # Don't override KoalaVim

        with open(dst, 'w') as out:
            out.write(_format_lazylock(content))

    print(f'{src} -> {dst}')

def _format_lazylock(content: dict) -> str:
    lines = ["{"]
    # json.dumps(content, out, indent=2)
    for plugin, plugin_content in content.items():
        plugin_content = json.dumps(plugin_content)
        plugin_content = plugin_content.replace('{', '{ ')
        plugin_content = plugin_content.replace('}', ' }')

        lines.append(f'  "{plugin}": {plugin_content},')

    # Remove trailing comma after last plugin
    lines[-1] = lines[-1][:-1]

    lines.append("}")

    return '\n'.join(lines)

LOCK_FILE = "lazy-lock.json"


def kvim_lockfile() -> Path:
    return kvim_dir() / LOCK_FILE


def user_lockfile() -> Path:
    return config_dir() / LOCK_FILE


def read_lockfile(path: Path) -> dict:
    with open(path / LOCK_FILE, 'r') as f:
        content = json.load(f)

        plugin_to_commit = {}
        for plugin, info in content.items():
            plugin_to_commit[plugin] = info['commit']

        return plugin_to_commit
