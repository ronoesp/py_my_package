
# 「setuptools」は標準ライブラリではないためインストールが必要
# pip install setuptools
from setuptools import setup, find_packages

setup(
    name='ono_commons',
    version='1.0',
    packages=find_packages()
)