#!/usr/bin/env bash
set -euo pipefail
set -x
docker compose build
docker compose run --rm run $*
