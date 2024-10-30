# SPDX-License-Identifier: GPL-3.0
# Apollo API
#
# src/lib/help.py
#
# COPYRIGHT NOTICE
# Copyright (C) 2024 0x4248 and contributors
# This file and software is licenced under the GNU General Public License v3.0. 
# Redistribution of this file and software is permitted under the terms of the 
# GNU General Public License v3.0. 
#
# NO WARRANTY IS PROVIDED WITH THIS SOFTWARE. I AM NOT RELIABLE FOR ANY DAMAGES.
# THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY AND LIABILITY OF ANY KIND.

class help:
    routes = []
    method = []
    description = []
    returns = []

def add_help(route, method, description, returns):
    help.routes.append(route)
    help.method.append(method)
    help.description.append(description)
    help.returns.append(returns)

def get_help(route):
    index = help.routes.index(route)
    return {"route": help.routes[index], "method": help.method[index], "description": help.description[index], "returns": help.returns[index]}

def get_all_help():
    return {"routes": help.routes, "methods": help.method, "description": help.description, "returns": help.returns}