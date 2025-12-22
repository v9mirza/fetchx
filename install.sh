#!/usr/bin/env bash
set -e

echo "Installing fetchx..."

# Ensure file exists
if [ ! -f "fetchx" ]; then
  echo "Error: fetchx file not found in current directory."
  exit 1
fi

# Install binary
sudo install -m 755 fetchx /usr/local/bin/fetchx

echo "fetchx installed successfully."
echo "Run: fetchx"
