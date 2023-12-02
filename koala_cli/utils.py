from pathlib import Path

def kvim_dir() -> Path:
    # TODO: [windows]
    return Path.home() / Path(".local/share/nvim/lazy/KoalaVim/")

def config_dir() -> Path:
    # TODO: [windows]
    return Path.home() / Path(".config/nvim/")
