from config import config_client as cfg
from Source.client import Client

plc_client = Client(cfg.plc_client_init, cfg.plc_tags)

plc_client.write_tag("SCADA", 20)
plc_client.read_tag("SCADA")
