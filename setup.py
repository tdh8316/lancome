from setuptools import setup, find_packages

import lancome

setup(
    name='lancome',
    version=lancome.__version__,
    packages=find_packages(exclude=['docs', 'tests*']),
    url='https://github.com/tdh8316/lancome',
    license='GNU General Public License v3.0',
    author='Donghyeok Tak',
    author_email='tdh8316@naver.com',
    description=open('./README.md', 'r', encoding='UTF-8').readlines()[1][:-2],
    long_description=open('README.md', 'r', encoding='UTF-8').read(),
    install_requires=['colorama'],
    python_requires='>=3',
)
