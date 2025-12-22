---

# 🚀 fetchx

**A minimal, dependency-free system information tool for Linux.**

`fetchx` provides essential system details in a clean, high-contrast layout. It is designed to be the first thing you see when you open your terminal—fast, readable, and out of your way.

---

##  Preview

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

```

---

## 💡 The fetchx Philosophy

Unlike other "fetch" tools that have grown into complex frameworks, `fetchx` follows the Unix philosophy of doing one thing well:

* **Zero Configuration:** No `.conf` files, no themes, no hidden folders.
* **Zero Dependencies:** Uses only the Python standard library. If you have Python, it works.
* **Zero Lag:** Optimized for execution in milliseconds to keep your shell responsive.
* **WSL Friendly:** Designed to detect and display Windows Subsystem for Linux environments correctly.

---

## 📥 Installation

### Quick Install

Install and set permissions with a single command:

```bash
curl -fsSL https://raw.githubusercontent.com/v9mirza/fetchx/main/install.sh | bash

```

### Manual Setup

If you prefer a manual installation to your local path:

```bash
git clone https://github.com/YOUR_USERNAME/fetchx.git
cd fetchx
chmod +x fetchx
mkdir -p ~/.local/bin
cp fetchx ~/.local/bin/

```

---

## 🛠 Usage

Simply run:

```bash
fetchx

```

To see your system info every time you open a terminal, add `fetchx` to your shell configuration:

```bash
# Add to .bashrc or .zshrc
echo "fetchx" >> ~/.zshrc

```

---

## 🗺 Roadmap

* [ ] **Side-by-side layout:** Better support for ultra-wide terminal windows.
* [ ] **Machine-readable:** Add a `--json` flag for integration into custom dashboards.
* [ ] **Native Packages:** `.deb` and `AUR` support.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

