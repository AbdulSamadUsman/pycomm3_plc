from pycomm3 import SHORT_STRING, REAL, INT

"""
Dictionary that is used for connection
"""
plc_client_init = {
    'ip': '192.168.18.38',
    'slot': 0}

# Dictionary used to read or write tags
plc_tags = {
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