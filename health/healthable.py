#!/usr/bin/env python3

from typing import Dict, List
from .types import Healthable, HealthGroup, HealthableVersion, HealthDecorator

from collections import defaultdict

HEALTHABLES: Dict[HealthGroup, List[Healthable]] = defaultdict(list)

def healthable(group: HealthGroup):
    def _inner_decorator(func: HealthDecorator):
        def _wrapper():
            # Translate exceptions as result errors
            try:
                return func()
            except Exception as e:
                return HealthableVersion.from_exception(e)

        HEALTHABLES[group].append(Healthable(func.__name__, _wrapper))
        return _wrapper

    return _inner_decorator
