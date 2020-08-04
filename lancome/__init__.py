import atexit
import sys
import time
import traceback

import colorama

from lancome.configure import configure
from lancome.formatter import ExceptionFormatter

__version__ = "0.1"


@atexit.register
def _dispose() -> None:
    time.sleep(0.1)  # Await socket
    colorama.deinit()


def _excepthook(t: type, v: Exception, tb) -> None:
    """Alternative of default sys.excepthook

    :param t: Exception type
    :param v: Exception value
    :param tb: Traceback
    :return: None
    """

    # time.sleep(0.1)  # Await socket
    fm = ExceptionFormatter.from_list(
        exception_messages=traceback.format_exception(t, v, tb)
    )

    fm.invoke()

    # time.sleep(0.1)  # Await socket
    # print("Original traceback:")
    # time.sleep(0.1)  # Await socket
    # traceback.print_tb(tb)


def init():
    sys.excepthook = lambda t, v, tb: _excepthook(t, v, tb)
    colorama.init(autoreset=True)
