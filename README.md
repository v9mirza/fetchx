
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

OS:        Ubuntu 24.04.3 LTS
Kernel:    6.6.x
Host:      acer
Packages:  693
Desktop:   tty
CPU:       AMD Ryzen 5 6600H
GPU:       Microsoft Basic Render Driver
Memory:    2.3GB / 7.5GB
Uptime:    16h 50m
Shell:     /bin/bash
Terminal:  xterm-256color
User:      mirza

```

---

## 🛠️ Usage & Commands

| Command | Description |
| --- | --- |
| `fetchx` | **Default**: Displays essential system snapshot. |
| `fetchx --full` | **Full Mode**: Extended details (Arch, Init, etc.). |
| `fetchx --network` | **Network Mode**: IP, MAC, Gateway, and DNS details. |
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
git clone [https://github.com/v9mirza/fetchx.git](https://github.com/v9mirza/fetchx.git)
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

* [ ] Side-by-side layout for ultra-wide terminals.
* [ ] JSON Output (`--json`) for scripting and dashboards.
* [ ] Native Packages via `.deb` and AUR.

---

**Released under the MIT License.**

```

