import os, time, psutil

def get_sys_load():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    return cpu, ram

def draw_bar(percent, width=20):
    filled = int(width * percent / 100)
    bar = "█" * filled + "░" * (width - filled)
    color = "\033[92m" if percent < 70 else "\033[93m" if percent < 90 else "\033[91m"
    return f"{color}[{bar}] {percent}%\033[0m"

cpu, ram = get_sys_load()
print(f"  CPU: {draw_bar(cpu)}")
print(f"  RAM: {draw_bar(ram)}")
