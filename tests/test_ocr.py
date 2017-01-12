from pathlib import Path

import config as cfg
import ocr


def test_ocr():
    img = str(Path(cfg.ASSETS_OCR_DIR, "fnord.png"))
    assert ocr.process(img).strip() == "fnord"
