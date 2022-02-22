from pycomm3 import LogixDriver
from pycomm3 import SHORT_STRING, REAL, INT

plc1 = LogixDriver("192.168.18.38", init_tags=False)
plc1._cfg["use_instance_ids"] = False
plc1._tags = {
        'SCADA': {
            'tag_name': 'SCADA',
            'tag_type': 'atomic',
            'data_type_name': 'INT',
            'data_type': 'INT',
            'dim': 1,
            'dimensions': [20, 0, 0],
            'type_class': INT,
        },
        'DECIMAL': {
            'tag_name': 'DECIMAL',
            'tag_type': 'atomic',
            'data_type_name': 'REAL',
            'data_type': 'REAL',
            'dim': 1,
            'dimensions': [100, 0, 0],
            'type_class': REAL,
        }
    }
print(plc1.tags)
plc1.open()
info = plc1.get_plc_info()
print(info)
wr1 = plc1.write("SCADA[0]{1}", 10)
print(wr1)
ret = plc1.read("SCADA{20}")
print(ret)
plc1.close()





