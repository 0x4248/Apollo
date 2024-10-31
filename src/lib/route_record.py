# SPDX-License-Identifier: GPL-3.0
# Apollo API
# A multi-purpose API.
#
# src/lib/route_record.py
# Records all the used routes in the API with their help information.
#
# COPYRIGHT NOTICE              
# Copyright (C) 2024 0x4248 and contributors
# This file and software is licenced under the GNU General Public License v3.0. 
# Redistribution of this file and software is permitted under the terms of the 
# GNU General Public License v3.0. 
#
# NO WARRANTY IS PROVIDED WITH THIS SOFTWARE. I AM NOT RELIABLE FOR ANY DAMAGES.
# THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY AND LIABILITY OF ANY KIND.


class RouteRecord:
	routes = [] 
	name = []
	method = []
	help = []

def record_route(route: str,
				 name: str,
				 method: str, 
				 help: str):
	RouteRecord.routes.append(route)
	RouteRecord.name.append(name)
	RouteRecord.method.append(method)
	RouteRecord.help.append(help)

def get_routes():
	return RouteRecord.routes, RouteRecord.name, RouteRecord.method, RouteRecord.help

def get_route(route: str):
	index = RouteRecord.routes.index(route)
	return RouteRecord.routes[index], RouteRecord.name[index], RouteRecord.method[index], RouteRecord.help[index]