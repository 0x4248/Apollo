# SPDX-License-Identifier: GPL-3.0
# Apollo API
#
# src/lib/modules.py
#
# COPYRIGHT NOTICE
# Copyright (C) 2024 0x4248 and contributors
# This file and software is licenced under the GNU General Public License v3.0. 
# Redistribution of this file and software is permitted under the terms of the 
# GNU General Public License v3.0. 
#
# NO WARRANTY IS PROVIDED WITH THIS SOFTWARE. I AM NOT RELIABLE FOR ANY DAMAGES.
# THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY AND LIABILITY OF ANY KIND.

import importlib

from lib.logger import logger
from lib.config import CONFIG

class apolloModule:
    modulesLoaded = []
    blueprintNames = []
    def load_module(module_name, blueprint_name, app):
        logger.log("Main -> apolloModule", f"Loading module {module_name}")
        module = importlib.import_module(module_name)
        blueprint = getattr(module, blueprint_name)
        app.register_blueprint(blueprint)
        apolloModule.modulesLoaded.append(module_name)
        apolloModule.blueprintNames.append(blueprint_name)
    def unload_module(module_name, app):
        apolloModule.modulesLoaded.remove(module_name)
        apolloModule.blueprintNames.remove(app.blueprints[module_name])
        app.blueprints.pop(module_name)
        del module_name

    def reload_all(app):            
        for module in apolloModule.modulesLoaded:
            apolloModule.unload_module(module, app)
            apolloModule.load_module(module, 
                                    apolloModule.blueprintNames[
                                        apolloModule.modulesLoaded.index(module)
                                    ], app)