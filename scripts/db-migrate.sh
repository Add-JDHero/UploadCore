#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$PROJECT_ROOT"

for migration in migrations/*.sql; do
  echo "Applying migration: $migration"
  docker exec -i uploadcore-postgres \
    psql -U uploadcore -d uploadcore \
    < "$migration"
done