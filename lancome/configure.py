from typing import Callable


class Configure(object):

    def __init__(self):
        self.use_color: bool = True

    @property
    def use_color(self) -> bool:
        return self.use_color

    @use_color.setter
    def use_color(self, value):
        self._use_color = value


def configure(use_color: bool = True):
    Configure.use_color = use_color

    return _Then


class _Then(object):

    @staticmethod
    def then(func: Callable):
        if callable(func):
            func()
        else:
            raise TypeError("{} is not callable.".format(func))
