# SPDX-License-Identifier: GPL-3.0
# Apollo API
#
# src/modules/ping.py
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
from lib.help import add_help

ping_bp = Blueprint('ping', __name__)

add_help("/api/ping", "GET", "Pings the server.", "String: Pong!")
@ping_bp.route('/api/ping')
async def ping():
    return "Pong!"

