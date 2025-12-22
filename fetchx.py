#!/usr/bin/env python3

import os
import platform

# ================= ASCII LOGO =================

ASCII_LOGO = r"""
   ███████╗███████╗████████╗ ██████╗██╗  ██╗██╗  ██╗
   ██╔════╝██╔════╝╚══██╔══╝██╔════╝██║  ██║╚██╗██╔╝
   █████╗  █████╗     ██║   ██║     ███████║ ╚███╔╝
   ██╔══╝  ██╔══╝     ██║   ██║     ██╔══██║ ██╔██╗
   ██║     ███████╗   ██║   ╚██████╗██║  ██║██╔╝ ██╗
   ╚═╝     ╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝
"""

# ================= HELPERS =================

def distro():
    try:
        with open("/etc/os-release") as f:
            for line in f:
                if line.startswith("PRETTY_NAME"):
                    return line.split("=")[1].strip().strip('"')
    except:
        pass
    return "unknown"

def uptime():
    with open("/proc/uptime") as f:
        seconds = float(f.readline().split()[0])
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    return f"{hours}h {minutes}m"

def memory():
    meminfo = {}
    with open("/proc/meminfo") as f:
        for line in f:
            key, val = line.split(":")
            meminfo[key] = int(val.strip().split()[0])

    total = meminfo["MemTotal"] // 1024
    available = meminfo["MemAvailable"] // 1024
    used = total - available
    return f"{used}MB / {total}MB"

def cpu():
    with open("/proc/cpuinfo") as f:
        for line in f:
            if "model name" in line:
                return line.split(":")[1].strip()
    return "unknown"

def arch():
    return platform.machine()

def desktop():
    return (
        os.environ.get("XDG_CURRENT_DESKTOP")
        or os.environ.get("DESKTOP_SESSION")
        or "tty"
    )

def terminal():
    return (
        os.environ.get("TERM_PROGRAM")
        or os.environ.get("TERM")
        or "unknown"
    )

def user():
    return os.environ.get("USER", "unknown")

# ================= MAIN =================

def main():
    os_name = platform.system()
    kernel = platform.release()
    host = platform.node()
    shell = os.environ.get("SHELL", "unknown")

    cyan = "\033[36m"
    reset = "\033[0m"

    print(f"{cyan}{ASCII_LOGO}{reset}")

    print(f"""
{cyan}OS:{reset}        {os_name}
{cyan}Distro:{reset}    {distro()}
{cyan}Kernel:{reset}    {kernel}
{cyan}Arch:{reset}      {arch()}
{cyan}Host:{reset}      {host}
{cyan}Desktop:{reset}   {desktop()}
{cyan}CPU:{reset}       {cpu()}
{cyan}Memory:{reset}    {memory()}
{cyan}Uptime:{reset}    {uptime()}
{cyan}Shell:{reset}     {shell}
{cyan}Terminal:{reset}  {terminal()}
{cyan}User:{reset}      {user()}
""")

if __name__ == "__main__":
    main()
