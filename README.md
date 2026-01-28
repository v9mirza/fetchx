
# 🚀 FetchX

**A minimal, dependency-free system information tool for Linux.**

---

## 📖 What is fetchx?

**fetchx** is a fast, no-nonsense system information fetcher for people who value clarity over clutter.

Most fetch tools started simple—and then accumulated themes, config files, plugins, and startup lag. `fetchx` deliberately moves in the opposite direction. 

It shows a clean, high-contrast snapshot of your system the moment your terminal opens, then gets out of the way. Written in **pure Python**, using **only the standard library**. If Python exists on your system, `fetchx` runs—no `pip`, no dependencies, no setup ceremony.

---

## 🖼️ Preview

```text
███████╗███████╗████████╗ ██████╗██╗  ██╗██╗  ██╗
██╔════╝██╔════╝╚══██╔══╝██╔════╝██║  ██║╚██╗██╔╝
█████╗  █████╗     ██║   ██║     ███████║ ╚███╔╝
██╔══╝  ██╔══╝     ██║   ██║     ██╔══██║ ██╔██╗
██║     ███████╗   ██║   ╚██████╗██║  ██║██╔╝ ██╗
╚═╝     ╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝


OS:        Arch Linux x86_64
Kernel:    6.12.10-arch1-1
Host:      acer
Packages:  1243 (pacman)
Desktop:   Hyprland
CPU:       AMD Ryzen 9 7950X
GPU:       NVIDIA GeForce RTX 4090
Memory:    4.2GB / 32.0GB
Disk:      205GB / 2.0TB (10%)
Battery:   100% (Full)
Uptime:    2d 4h 12m
Shell:     /bin/zsh
Terminal:  kitty
User:      mirza

```

---

## 🛠️ Usage & Commands

| Command | Description |
| --- | --- |
| `fetchx` | **Default**: Displays essential system snapshot. |
| `fetchx --full` | **Full Mode**: Extended details (Arch, Init, etc.). |
| `fetchx --network` | **Network Mode**: IP, MAC, Gateway, and DNS details. |
| `fetchx --compact` | **Compact Mode**: Single-line output for status bars. |
| `fetchx --json` | **JSON Output**: Machine-readable format for scripts. |
| `fetchx --help` | **Help**: Displays all available flags and usage. |
| `fetchx --version` | **Version**: Shows current installed version. |

---

## 💡 Design Philosophy

* **Zero configuration** — No dotfiles, no hidden state.
* **Zero dependencies** — Python 3 standard library only.
* **Zero lag** — Optimized for instant execution.
* **WSL-aware** — Detects and adapts to Windows Subsystem for Linux.

---

## 📥 Installation

### Quick Install (Recommended)

```bash
curl -fsSL https://raw.githubusercontent.com/v9mirza/fetchx/main/install.sh | bash

```

### Manual Setup

```bash
git clone https://github.com/v9mirza/fetchx.git
cd fetchx
chmod +x fetchx
mkdir -p ~/.local/bin
cp fetchx ~/.local/bin/

```

*Note: Ensure `~/.local/bin` is in your `$PATH`.*

---

## ⚙️ Optional: Auto-run on Terminal Launch

To have `fetchx` greet you every time you open a terminal, add this to your `~/.bashrc` or `~/.zshrc`:

```bash
if [[ $SHLVL -eq 1 ]] && command -v fetchx >/dev/null; then
  fetchx
fi

```

---

## 🗺️ Roadmap

* [x] JSON Output (`--json`) for scripting and dashboards.
* [x] Hardware Metrics (Disk Usage, Battery).
* [x] Performance Optimization (Fast package counting).
* [x] Compact Mode (`--compact`).
* [ ] Side-by-side layout for ultra-wide terminals.
* [ ] Native Packages via `.deb` and AUR.

---

**Released under the MIT License.**
```

