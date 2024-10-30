# SPDX-License-Identifier: GPL-3.0
# Apollo API
#
# src/lib/logger.py
#
# COPYRIGHT NOTICE
# Copyright (C) 2024 0x4248 and contributors
# This file and software is licenced under the GNU General Public License v3.0. 
# Redistribution of this file and software is permitted under the terms of the 
# GNU General Public License v3.0. 
#
# NO WARRANTY IS PROVIDED WITH THIS SOFTWARE. I AM NOT RELIABLE FOR ANY DAMAGES.
# THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY AND LIABILITY OF ANY KIND.

import datetime
import json

class log_levels:
    LOG = 0
    INFO = 1
    WARN = 2
    ERROR = 3
    CRITICAL = 4
    
def update_log_record(module, message, level):
    try:
        with open("data/log.json", "r") as f:
            log = json.load(f)
    except:
        log = []

    log.append([str(datetime.datetime.now()), level, module, message])

    with open("data/log.json", "w") as f:
        json.dump(log, f, indent=4)
    
class logger:
    def log(module, message):
        print(f"[LOG] {module}: {message}")
        update_log_record(module, message, log_levels.LOG)
    
    def error(module, message):
        print(f"[ERROR] {module}: {message}")
        update_log_record(module, message, log_levels.ERROR)
    
    def warn(module, message):
        print(f"[WARN] {module}: {message}")
        update_log_record(module, message, log_levels.WARN)
    
    def info(module, message):
        print(f"[INFO] {module}: {message}")
        update_log_record(module, message, log_levels.INFO)