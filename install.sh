#!/usr/bin/env bash
set -e

REPO="v9mirza/fetchx"
RAW_BASE="https://raw.githubusercontent.com/$REPO/main"
BIN_NAME="fetchx"
INSTALL_PATH="/usr/local/bin/$BIN_NAME"

echo "Installing fetchx..."

# Download fetchx
tmp_dir="$(mktemp -d)"
curl -fsSL "$RAW_BASE/fetchx" -o "$tmp_dir/$BIN_NAME"

# Verify download
if [ ! -s "$tmp_dir/$BIN_NAME" ]; then
  echo "Error: failed to download fetchx"
  exit 1
fi

# Install
sudo install -m 755 "$tmp_dir/$BIN_NAME" "$INSTALL_PATH"

# Cleanup
rm -rf "$tmp_dir"

echo "fetchx installed successfully."
echo "Run: fetchx"
