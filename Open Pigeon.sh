#!/bin/sh
set -eu
cd "$(dirname "$0")"
exec python3 tools/pigeon_gui.py
