# SPDX-License-Identifier: GPL-3.0
# Apollo API
#
# src/modules/help.py
#
# COPYRIGHT NOTICE
# Copyright (C) 2024 0x4248 and contributors
# This file and software is licenced under the GNU General Public License v3.0. 
# Redistribution of this file and software is permitted under the terms of the 
# GNU General Public License v3.0. 
#
# NO WARRANTY IS PROVIDED WITH THIS SOFTWARE. I AM NOT RELIABLE FOR ANY DAMAGES.
# THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY AND LIABILITY OF ANY KIND.


from flask import Blueprint, jsonify

from lib.help import add_help, get_help, get_all_help

help_bp = Blueprint('help', __name__)

add_help("/help", "GET", "Show all routes", "JSON: Returns all routes in the API.")
@help_bp.route('/help')
def help():
    return jsonify(get_all_help())
    