import re
from typing import List, Iterable

from colorama import Fore, Back

from lancome.configure import Configure


class ExceptionFormatter(object):
    """"""

    def __init__(self):
        self.messages: list = []

    @classmethod
    def from_list(cls, exception_messages: List[str]):
        self = cls()

        exception_messages: Iterable = ''.join(exception_messages).split('\n')[1:]

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
        if Configure.use_color:
            print(Back.RED + Fore.WHITE + " An unhandled exception was occurred. ")
        else:
            print(" An unhandled exception was occurred. ")
        for messages in self.messages[:-1]:
            messages: list = [s.strip() for s in messages if s != '']

            scope: str = messages[0]
            statement: str = messages[1]

            info = re.match(r"File \"(?P<fn>.+)\", line (?P<line>\d+), in (?P<scope>.+)", scope)

            if hasattr(info, "group"):
                if Configure.use_color:
                    print(
                        "{3}{0} {5}{2}\n{4}{1}| {6}{7}\n".format(
                            info.group("fn"), info.group("line"), info.group("scope"),
                            Fore.LIGHTBLUE_EX, Fore.YELLOW, Fore.MAGENTA,
                            Fore.RESET, statement,
                            # "~"*len(statement)
                        ),
                    )
                else:
                    print(
                        "{3}{0} {5}{2}\n{4}{1}| {6}{7}\n".format(
                            info.group("fn"), info.group("line"), info.group("scope"),
                            '', '', '',
                            Fore.RESET, statement,
                            # "~"*len(statement)
                        ),
                    )
            else:
                err: str = messages[0]
                scope: str = messages[-2]
                statement: str = messages[-1]
                info = re.match(r"File \"(?P<fn>.+)\", line (?P<line>\d+), in (?P<scope>.+)", scope)
                if Configure.use_color:
                    print(
                        Fore.RED + err
                    )
                    print(Back.RED + Fore.WHITE + " {} ".format(messages[1]))
                    print(
                        "{3}{0} {5}{2}\n{4}{1}| {6}{7}\n".format(
                            info.group("fn"), info.group("line"), info.group("scope"),
                            Fore.LIGHTBLUE_EX, Fore.YELLOW, Fore.MAGENTA,
                            Fore.RESET, statement,
                            # "~"*len(statement)
                        ),
                    )
                else:
                    print(
                        '' + err
                    )
                    print(" {} ".format(messages[1]))
                    print(
                        "{3}{0} {5}{2}\n{4}{1}| {6}{7}\n".format(
                            info.group("fn"), info.group("line"), info.group("scope"),
                            '', '', '',
                            Fore.RESET, statement,
                            # "~"*len(statement)
                        ),
                    )
        if Configure.use_color:
            print(
                Fore.RED + self.messages[-1][0]
            )
        else:
            print(
                self.messages[-1][0]
            )
