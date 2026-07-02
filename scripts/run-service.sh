#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$PROJECT_ROOT"

echo "Project root: $PROJECT_ROOT"
echo "Starting UploadCore..."

exec ./build-debug/UploadCore --config configs/static_config.yaml --config_vars configs/config_vars.yaml