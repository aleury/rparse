#!/usr/bin/env python
from distutils.core import setup


def load_requirements():
    with open("requirements.txt") as requirements:
        return requirements.read().splitlines()


setup(name="rparse",
      version="0.1.0",
      description="Python requirements.txt parser",
      author="Dmitry Veselov",
      author_email="d.a.veselov@yandex.ru",
      url="https://github.com/dveselov/rparse",
      py_modules=["rparse"],
      install_requires=load_requirements(),
      classifiers=[
          "Intended Audience :: Developers",
          "Development Status :: 1 - Planning",
          "License :: OSI Approved :: MIT License",

          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.4",

          "Programming Language :: Python :: Implementation :: CPython",
          "Programming Language :: Python :: Implementation :: PyPy",
      ],
     )