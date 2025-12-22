# 🚀 fetchx

**A minimal, dependency-free system information tool for Linux.**

`fetchx` provides essential system details in a clean, high-contrast layout.  
It is designed to be fast, readable, and out of your way.

---

## 🖼️ Preview

```text
███████╗███████╗████████╗ ██████╗██╗  ██╗██╗  ██╗
██╔════╝██╔════╝╚══██╔══╝██╔════╝██║  ██║╚██╗██╔╝
█████╗  █████╗     ██║   ██║     ███████║ ╚███╔╝
██╔══╝  ██╔══╝     ██║   ██║     ██╔══██║ ██╔██╗
██║     ███████╗   ██║   ╚██████╗██║  ██║██╔╝ ██╗
╚═╝     ╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝

OS:        Linux
Distro:    Ubuntu 24.04 LTS
Kernel:    6.6.x
Arch:      x86_64
CPU:       Ryzen 5 6600H
Memory:    3.2GB / 7.5GB
Uptime:    13h 20m
Shell:     zsh
````

---

## 💡 The fetchx Philosophy

Unlike other “fetch” tools that have grown into complex frameworks, `fetchx`
follows the Unix philosophy of doing one thing well:

* **Zero Configuration** — No `.conf` files, no themes, no hidden folders.
* **Zero Dependencies** — Uses only the Python standard library (Python 3 required).
* **Zero Lag** — Optimized for execution in milliseconds.
* **WSL Friendly** — Correctly detects Windows Subsystem for Linux environments.

---

## 📥 Installation

### Requirements

* Linux (or WSL)
* Python 3.8+

### Quick Install

Install system-wide with a single command:

```bash
curl -fsSL https://raw.githubusercontent.com/v9mirza/fetchx/main/install.sh | bash
```

---

### Manual Setup

If you prefer a manual installation to your local path:

```bash
git clone https://github.com/v9mirza/fetchx.git
cd fetchx
chmod +x fetchx
mkdir -p ~/.local/bin
cp fetchx ~/.local/bin/
```

Make sure `~/.local/bin` is in your `PATH`.

---

## 🛠 Usage

Run:

```bash
fetchx
```

### Optional: Run on Terminal Startup (Safe)

If you want `fetchx` to run when you open a terminal, add this **at the end**
of your shell config file:

```bash
# ~/.bashrc or ~/.zshrc
if [[ $SHLVL -eq 1 ]] && command -v fetchx >/dev/null; then
  fetchx
fi
```

This avoids startup warnings and runs only once per terminal session.

---

## 🗺 Roadmap

* [ ] Side-by-side layout for wide terminals
* [ ] Machine-readable output (`--json`)
* [ ] Native packages (`.deb`, AUR)

---

## 📄 License

Distributed under the MIT License.
See the `LICENSE` file for details.

```