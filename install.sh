#!/usr/bin/env bash
set -e

# -------------------------------
# Dependency check
# -------------------------------
if ! command -v python3 >/dev/null; then
  echo "Error: python3 is required but not installed."
  echo
  echo "Install Python 3 using your package manager:"
  echo "  Debian/Ubuntu : sudo apt install python3"
  echo "  Fedora/RHEL   : sudo dnf install python3"
  echo "  Arch Linux    : sudo pacman -S python"
  exit 1
fi

# -------------------------------
# Config
# -------------------------------
REPO="v9mirza/fetchx"
RAW_BASE="https://raw.githubusercontent.com/$REPO/main"
BIN_NAME="fetchx"
INSTALL_PATH="/usr/local/bin/$BIN_NAME"

echo "Installing fetchx..."

# -------------------------------
# Download
# -------------------------------
tmp_dir="$(mktemp -d)"
curl -fsSL "$RAW_BASE/$BIN_NAME" -o "$tmp_dir/$BIN_NAME"

if [ ! -s "$tmp_dir/$BIN_NAME" ]; then
  echo "Error: failed to download fetchx"
  rm -rf "$tmp_dir"
  exit 1
fi

# -------------------------------
# Install
# -------------------------------
sudo install -m 755 "$tmp_dir/$BIN_NAME" "$INSTALL_PATH"

# -------------------------------
# Cleanup
# -------------------------------
rm -rf "$tmp_dir"

echo "fetchx installed successfully."
echo "Run: fetchx"
