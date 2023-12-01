#!/usr/bin/env python3

from pathlib import Path

from git import Repo

def kvim_dir() -> Path:
    # TODO: [windows]
    return Path.home() / Path(".local/share/nvim/lazy/KoalaVim/")

def config_dir() -> Path:
    # TODO: [windows]
    return Path.home() / Path(".config/nvim/")

def data_dir() -> Path:
    # TODO: [windows]
    return Path.home() / Path(".local/share/KoalaVim")

def kvim_repo() -> Repo:
    return Repo(kvim_dir())
