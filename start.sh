#!/usr/bin/env bash
# Run the Flask app from the directory of this script so it works from any location.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$SCRIPT_DIR/app.py" "$@"
