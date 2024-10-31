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

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from asyncio import run
import uvicorn
import importlib

from lib.route_record import get_routes
import lib.logger as logger

app = FastAPI()

modules = ["modules.ping"]

for module in modules:
    mod = importlib.import_module(module)
    app.include_router(mod.router)

@app.get("/")
async def root():
    return get_routes()

@app.middleware("http")
async def log_request_info(request: Request, call_next):
    logger.info("Request", f"Request made to {request.url}")
    response = await call_next(request)
    return response

if __name__ == "__main__":
    logger.logs_init()
    uvicorn.run(app, host="0.0.0.0", port=8000, server_header="Apollo API", log_level="error")