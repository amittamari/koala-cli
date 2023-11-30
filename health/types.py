#!/usr/bin/env python3

from typing import Callable, NamedTuple, Optional
from enum import Enum

SemVer = str

class HealthableVersion(NamedTuple):
    ver: Optional[SemVer] = None
    commit: Optional[str] = None
    error: Optional[str] = None

    @staticmethod
    def from_exception(e: Exception):
        return HealthableVersion(ver=None, commit=None, error=str(e))

    def __str__(self):
        if self.ver is None and self.commit is None and self.error is None:
            return 'Healthy'

        if self.error is not None:
            return f'[bold red]{self.error}'

        # TODO: compare versions with lock file

        return f'{self.ver or ""} {self.commit or ""}'

HealthDecorator = Callable[[], HealthableVersion]

class Healthable(NamedTuple):
    name: str
    check_health: HealthDecorator

HealthGroup = Enum('HealthGroup', ['core', 'dependencies'])
