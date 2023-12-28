#!/usr/bin/env python3

import subprocess
from collections import defaultdict
from typing import Dict, List, Tuple

import re
import typer
from rich.console import Console
from rich.table import Table

from .healthable import HEALTHABLES, healthable
from .types import Healthable, HealthableVersion, HealthGroup

app = typer.Typer(help="Check KoalaVim's health")


@app.callback(invoke_without_command=True)
def health():
    # TODO: show lockfile status

    results: Dict[
        HealthGroup, List[Tuple[Healthable, HealthableVersion]]
    ] = defaultdict(list)

    for group, healthables in HEALTHABLES.items():
        for h in healthables:
            res = h.check_health()
            results[group].append((h, res))

    for group, group_results in results.items():
        print_group_results(group, group_results)


def print_group_results(
    group: HealthGroup, results: List[Tuple[Healthable, HealthableVersion]]
):
    table = Table(title=group.name)
    table.add_column('Entity', style='medium_purple')
    table.add_column('Result', style='green')
    for h, res in results:
        table.add_row(h.name, str(res))

    console = Console()
    console.print(table)


@healthable(HealthGroup.core)
def nvim() -> HealthableVersion:
    output = subprocess.check_output(['nvim', '--version']).splitlines()
    m = re.match(r'NVIM v([\d\.]*)(?:.*?([a-e0-9]{7}))?', output[0].decode())

    return HealthableVersion(m.group(1), m.group(2))


@healthable(HealthGroup.dependencies)
def ripgrep() -> HealthableVersion:
    output = subprocess.check_output(['rg', '--version']).splitlines()
    m = re.match(r'ripgrep ([\d\.]*)', output[0].decode())

    return HealthableVersion(m.group(1), commit=None)


@healthable(HealthGroup.dependencies)
def fd() -> HealthableVersion:
    output = subprocess.check_output(['fd', '--version']).decode()
    m = re.match(r'fd ([\d\.]*)', output)

    return HealthableVersion(m.group(1), commit=None)


@healthable(HealthGroup.dependencies)
def fzf() -> HealthableVersion:
    output = subprocess.check_output(['fzf', '--version']).decode()
    m = re.match(r'([\d\.]*) \((.*)\)', output)

    return HealthableVersion(m.group(1), m.group(2))


@healthable(HealthGroup.dependencies)
def nerd_font() -> HealthableVersion:
    output = subprocess.check_output(['fc-list']).decode().splitlines()
    for line in output:
        if 'Nerd Font' in line:
            return HealthableVersion()

    # TODO better exception group
    raise Exception("Nerd Font not found")


if __name__ == '__main__':
    app()
