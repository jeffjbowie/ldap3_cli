#! /usr/bin/env python3

from ldap3 import Server, Connection, ALL
import pdb
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("server", help="Server Address")
parser.add_argument("domain", help="Domain Name")
parser.add_argument("user", help="Username")
parser.add_argument("password", help="Password")

server = parser.parse_args().server
domain = parser.parse_args().domain
user = domain + "\\" + parser.parse_args().user
password = parser.parse_args().password

server = Server(server,  get_info=ALL)

try:
	conn = Connection(server, user=user, password=password, auto_bind=True)
	conn.start_tls()
	if conn.bind():
		print("success")
except Exception:
	print("failure")










