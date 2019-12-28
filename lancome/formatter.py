import re
from typing import List

from colorama import Fore, Back


class ExceptionFormatter(object):
    """"""

    def __init__(self):
        self.messages: list = []

    @classmethod
    def from_list(cls, exception_messages: List[str]):
        self = cls()

        exception_messages = ''.join(exception_messages).split('\n')[1:]

        formatted_messages: List = []
        latest_indention: int = 0

        for i, message in enumerate(exception_messages):
            current_indention = len(message) - len(message.lstrip()) + 1

            if current_indention >= latest_indention:
                if len(formatted_messages) > 0:
                    formatted_messages[-1].append(message)
                else:
                    formatted_messages.append([message])
            else:
                formatted_messages.append([message])

            latest_indention = current_indention
            continue

        self.messages = formatted_messages

        return self

    def invoke(self) -> None:
        print(Back.RED + Fore.WHITE + " An unhandled exception was occurred. ")
        for messages in self.messages[:-1]:
            messages: list = [s.strip() for s in messages if s != '']

            scope: str = messages[0]
            statement: str = messages[1]

            info = re.match(r"File \"(?P<fn>.+)\", line (?P<line>\d+), in (?P<scope>.+)", scope)

            if hasattr(info, "group"):
                print(
                    "{3}{0} {5}{2}\n{4}{1}| {6}{7}\n".format(
                        info.group("fn"), info.group("line"), info.group("scope"),
                        Fore.BLUE, Fore.YELLOW, Fore.MAGENTA,
                        Fore.BLACK, statement,
                        # "~"*len(statement)
                    ),
                )
            else:
                print('\n'.join(messages), end='\n' * 2)
        print(
            Fore.RED + self.messages[-1][0]
        )
