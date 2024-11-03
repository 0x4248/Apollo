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
from fastapi.responses import JSONResponse, PlainTextResponse
from asyncio import run
import uvicorn
import importlib
import time

import lib.logger as logger

app = FastAPI()

modules = ["modules.ping"]

for module in modules:
    mod = importlib.import_module(module)
    app.include_router(mod.router)

@app.get("/")
async def root():
    return str(app.routes)

@app.middleware("http")
async def log_request_info(request: Request, call_next):
    logger.info("Request", f"Request made to {request.url}")
    pre_reqtime = time.time()
    response = await call_next(request)
    post_reqtime = time.time()
    response.headers["server"] = "Apollo"
    response.headers["apollo-version"] = "0.1"
    response.headers["compute-time"] = str(post_reqtime - pre_reqtime)

    return response

if __name__ == "__main__":
    logger.logs_init()
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="error")