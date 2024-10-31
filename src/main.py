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
import importlib
import logging
import json


from lib.logger import logger

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
del log

class apolloModule:
    modulesLoaded = []
    blueprintNames = []
    def load_module(module_name, blueprint_name):
        logger.log("Main -> apolloModule", f"Loading module {module_name}")
        module = importlib.import_module(module_name)
        blueprint = getattr(module, blueprint_name)
        app.register_blueprint(blueprint)
        apolloModule.modulesLoaded.append(module_name)
        apolloModule.blueprintNames.append(blueprint_name)
    def unload_module(module_name):
        apolloModule.modulesLoaded.remove(module_name)
        apolloModule.blueprintNames.remove(app.blueprints[module_name])
        app.blueprints.pop(module_name)
        del module_name

    def reload_all():               
        for module in apolloModule.modulesLoaded:
            apolloModule.unload_module(module)
            apolloModule.load_module(module, 
                                    apolloModule.blueprintNames[
                                        apolloModule.modulesLoaded.index(module)
                                    ])

apolloModule.load_module("modules.ping", "ping_bp")
apolloModule.load_module("modules.help", "help_bp")

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
    app.run(port=5000)
    logger.log("Main", "Apollo API started on http://localhost:5000")