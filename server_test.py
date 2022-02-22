"""
Server test which utilize server.py module and demonstrate server tag setup
"""

from config import config_server as cfg
from Source.server import Server

plc_client = Server(cfg.plc_server_init)
plc_client.connect()
