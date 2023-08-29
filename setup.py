#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="mvr-uuid-shuffle",
    version="0.0.1",
    py_modules=["mvrUuidShuffle"],
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "mvrUuidShuffle = mvrUuidShuffle:mvrUuidShuffle",
        ],
    },
)
