# fetchx
Fetchx

Fetchx is a fast, minimal system information tool for Linux.
It displays essential system details in a clean, neofetch-style layout — nothing more, nothing less.

Built to be readable, hackable, and honest.

Why Fetchx?

Most fetch tools fall into one of two traps:

Too minimal to be useful

Too decorative to be trustworthy

Fetchx sits in the middle.

It shows only what you actually care about when you open a terminal:

What system am I on?

What am I running?

How long has it been alive?

No plugins. No config files. No noise.

Features

Linux-first (native + WSL)

Zero dependencies (Python standard library only)

Instant execution

Always-on ASCII header

Clean, readable output

One-file design

Example Output
███████╗███████╗████████╗ ██████╗██╗  ██╗██╗  ██╗
██╔════╝██╔════╝╚══██╔══╝██╔════╝██║  ██║╚██╗██╔╝
█████╗  █████╗     ██║   ██║     ███████║ ╚███╔╝
██╔══╝  ██╔══╝     ██║   ██║     ██╔══██║ ██╔██╗
██║     ███████╗   ██║   ╚██████╗██║  ██║██╔╝ ██╗
╚═╝     ╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝

OS:        Linux
Distro:    Arch Linux
Kernel:    6.6.x
Arch:      x86_64
Host:      acer
Desktop:   KDE
CPU:       Ryzen 5 6600H
Memory:    3.3GB / 7.5GB
Uptime:    2h 14m
Shell:     /usr/bin/zsh
Terminal:  xterm-256color
User:      mirza

Installation
Requirements

Linux (or WSL)

Python 3.8+

Install
git clone https://github.com/yourusername/fetchx.git
cd fetchx
chmod +x fetchx.py
sudo mv fetchx.py /usr/local/bin/fetchx


Run:

fetchx

Philosophy

Fetchx follows three rules:

Essentials only
If it’s not useful every time, it doesn’t belong.

Truth over polish
Fetchx reports what the system exposes — no guesses, no cosmetics.

Readable code
The source should be as clear as the output.

What Fetchx Is Not

Not a distro showcase

Not a theming engine

Not a plugin framework

Not a replacement for neofetch

Fetchx is a system fingerprint, not a banner.

Roadmap (Intentional, Not Promised)

Side-by-side layout (logo + info)

Optional flags (--json, --no-color)

GPU detection (carefully)

Config support (v2)

Only additions that respect the core philosophy will be accepted.

Contributing

Contributions are welcome if they align with the project goals.

Before opening a PR, ask:

“Would this be useful every single time Fetchx runs?”

If the answer isn’t yes, it probably doesn’t belong.

License

MIT License.

Use it. Fork it. Modify it.
Just don’t turn it into noise.