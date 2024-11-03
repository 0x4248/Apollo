# SPDX-License-Identifier: GPL-3.0
# Apollo API
# A multi-purpose API.
#
# src/modules/http_codes.py
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
from fastapi import status


router = APIRouter()

@router.get("/codes/200", description="Returns a 200 OK response.")
async def code_200():
	return PlainTextResponse("200 OK")

@router.get("/codes/201", description="Returns a 201 Created response.")
async def code_201():
	return PlainTextResponse("201 Created")