#!/usr/bin/env python
import os
from swampdragon.swampdragon_server import run_server

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meetupdemo.settings")

run_server()