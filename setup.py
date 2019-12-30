from setuptools import setup

import lancome

setup(
    name='lancome',
    version=lancome.__version__,
    packages=[''],
    url='https://github.com/tdh8316/lancome',
    license='GNU General Public License v3.0',
    author='Donghyeok Tak',
    author_email='tdh8316@naver.com',
    description=open("./README.md", 'r', encoding="UTF-8").readlines()[1][:-2],
    install_requires=['colorama']
)
