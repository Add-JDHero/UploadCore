#!/usr/bin/env bash
set -euo pipefail

cd /workspace/UploadCore

mkdir -p logs
touch logs/service.log

tail -f logs/service.log | python3 scripts/pretty-tskv.py
