#!/usr/bin/env bash
set -euo pipefail

docker exec -it uploadcore-postgres \
  psql -U uploadcore -d uploadcore