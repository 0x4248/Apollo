# SPDX-License-Identifier: GPL-3.0
# Apollo API
# A multi-purpose API.
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

import traceback
import datetime
import json
import os

def logs_init() -> None:
	if not os.path.exists("data/logs"):
		os.makedirs("data/logs")

	if not os.path.exists("data/logs/log.csv"):
		with open("data/logs/log.csv", "w") as f:
			f.write("time,level,caller,message\n")

def handle_log(caller=None, msg=None, level=None) -> None:
	if caller is None:
		caller = traceback.extract_stack(None, 2)[0].name
	time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	log_output = f"{time},{level},{caller},{msg}"

	with open("data/logs/log.csv", "a") as f:
		f.write(log_output)
		f.write("\n")
	
	print(f"[{time}] {level}: {caller}: {msg}")

def log(caller=None, msg=None) -> None:
	handle_log(caller, msg, "LOG")

def error(caller=None, msg=None) -> None:
	handle_log(caller, msg, "ERROR")

def debug(caller=None, msg=None) -> None:
	handle_log(caller, msg, "DEBUG")

def warn(caller=None, msg=None) -> None:
	handle_log(caller, msg, "WARN")

def info(caller=None, msg=None) -> None:
	handle_log(caller, msg, "INFO")

def critical(caller=None, msg=None) -> None:
	handle_log(caller, msg, "CRITICAL")
