import os
from pathlib import Path


ROOT_DIR = os.path.dirname(__file__)

USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0'

MPLAYER = '/usr/bin/mplayer'
PLAYER = MPLAYER
TESSERACT = '/usr/bin/tesseract'
XSEL = '/usr/bin/xsel'
YOUTUBE_DL = '/usr/bin/youtube-dl'
FFMPEG = '/usr/bin/ffmpeg'
FILE = '/usr/bin/file'
ICONV = '/usr/bin/iconv'

ASSETS_DIR = str(Path(ROOT_DIR, 'assets'))
ASSETS_OCR_DIR = str(Path(ROOT_DIR, 'assets', 'ocr'))
