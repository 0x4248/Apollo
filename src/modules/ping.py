# SPDX-License-Identifier: GPL-3.0
# Apollo API
# A multi-purpose API.
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

from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from lib.route_record import record_route

router = APIRouter()

record_route("/ping", "ping", "GET", "Pings the server.")
@router.get("/ping")
async def ping():
	return PlainTextResponse("pong")