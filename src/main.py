# SPDX-License-Identifier: GPL-3.0
# Apollo API
# A multi-purpose API.
#
# src/main.py
#
# COPYRIGHT NOTICE              
# Copyright (C) 2024 0x4248 and contributors
# This file and software is licenced under the GNU General Public License v3.0. 
# Redistribution of this file and software is permitted under the terms of the 
# GNU General Public License v3.0. 
#
# NO WARRANTY IS PROVIDED WITH THIS SOFTWARE. I AM NOT RELIABLE FOR ANY DAMAGES.
# THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY AND LIABILITY OF ANY KIND.

from flask import Flask, jsonify, request
from asyncio import run

import logging
import json


from lib.logger import logger
from lib.config import CONFIG
from lib.modules import apolloModule

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
del log

apolloModule.load_module("modules.ping", "ping_bp", app)
apolloModule.load_module("modules.help", "help_bp", app)

@app.route('/')
async def index():
    return jsonify({"modules": apolloModule.modulesLoaded}) 

@app.route('/log')
async def ping():
    with open("data/log.json", "r") as f:
        log = json.load(f)
    return jsonify(log)

@app.before_request
async def log_request_info():
    logger.log("Main", f"Request to {request.path}")

if __name__ == '__main__':
    logger.log("Main", f"Apollo API started on http://localhost:{CONFIG.PORT}")
    app.run(port=CONFIG.PORT, debug=CONFIG.DEBUG)