from setuptools import setup, find_packages

import lancome

setup(
    name='lancome',
    version=lancome.__version__,
    packages=find_packages(exclude=['docs', 'tests*']),
    url='https://github.com/tdh8316/lancome',
    license='MIT License',
    author='Donghyeok Tak',
    author_email='tdh8316@naver.com',
    description="Lancôme, The choice to fill your exception outputs with beauty.",
    long_description=open('README.md', encoding='UTF-8').read(),
    install_requires=['colorama'],
    python_requires='>=3',
)
