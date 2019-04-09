#!/usr/bin/env python
# coding: utf-8

# Copyright (c) 2002-2016 "Neo Technology,"
# Network Engine for Objects in Lund AB [http://neotechnology.com]
#
# This file is part of Neo4j.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from setuptools import setup, find_packages


packages = find_packages(exclude=("test", "test.*"))
package_metadata = {
    "name": "theresa",
    "version": "0.0",
    "description": "Theresa May simulator",
    "author": "Nigel Small",
    "author_email": "technige@nige.tech",
    "entry_points": {
        "console_scripts": [
            "theresa = theresa.__main__:main",
        ],
    },
    "packages": packages,
    "install_requires": [
        "six",
    ],
    "license": "Apache License, Version 2.0",
    "classifiers": [
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
}

setup(**package_metadata)
