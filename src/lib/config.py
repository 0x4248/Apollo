# SPDX-License-Identifier: GPL-3.0
# Apollo API
#
# src/lib/config.py
#
# COPYRIGHT NOTICE
# Copyright (C) 2024 0x4248 and contributors
# This file and software is licenced under the GNU General Public License v3.0. 
# Redistribution of this file and software is permitted under the terms of the 
# GNU General Public License v3.0. 
#
# NO WARRANTY IS PROVIDED WITH THIS SOFTWARE. I AM NOT RELIABLE FOR ANY DAMAGES.
# THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY AND LIABILITY OF ANY KIND.

import configparser

# Create the configparser object
config = configparser.ConfigParser()

config.read('config.ini')

class CONFIG:
	PORT = config['DEFAULT']['PORT']
	DEBUG = config['DEFAULT']['DEBUG']
	MODULES = config['DEFAULT']['MODULES']