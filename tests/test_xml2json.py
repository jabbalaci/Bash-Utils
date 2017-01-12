import json
from pathlib import Path

import config as cfg
import xml2json


DICT = {
    "note": {
        "to": "Tove",
        "from": "Jani",
        "heading": "Reminder",
        "body": "Don't forget me this weekend!"
    }
}

def test_convert():
    xml_file = str(Path(cfg.ASSETS_DIR, "note.xml"))
    json_output = xml2json.convert(xml_file)
    d = json.loads(json_output)
    assert d == DICT
