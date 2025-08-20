import psutil
import GPUtil
import time
import tkinter as tk

def get_system_stats(frame_count, start_time):
    # CPU usage
    cpu_usage = psutil.cpu_percent(interval=0)

    # RAM usage
    ram = psutil.virtual_memory()
    ram_usage = ram.percent
    ram_used = round(ram.used / (1024 ** 3), 2)
    ram_total = round(ram.total / (1024 ** 3), 2)

    # GPU stats
    gpus = GPUtil.getGPUs()
    if gpus:
        gpu = gpus[0]
        gpu_load = gpu.load * 100
        gpu_temp = gpu.temperature
        gpu_mem_used = round(gpu.memoryUsed, 2)
        gpu_mem_total = round(gpu.memoryTotal, 2)
    else:
        gpu_load = gpu_temp = gpu_mem_used = gpu_mem_total = "N/A"

    # FPS
    elapsed_time = time.time() - start_time
    fps = frame_count / elapsed_time if elapsed_time > 0 else 0

    return {
        "FPS": f"{fps:.2f}",
        "CPU": f"{cpu_usage}%",
        "RAM": f"{ram_usage}% ({ram_used}GB/{ram_total}GB)",
        "GPU Load": f"{gpu_load}%",
        "GPU Temp": f"{gpu_temp}°C",
        "GPU Mem": f"{gpu_mem_used}MB/{gpu_mem_total}MB"
    }

def update_stats():
    global frame_count
    frame_count += 1
    stats = get_system_stats(frame_count, start_time)

    for key, label in labels.items():
        label.config(text=f"{key}: {stats[key]}")

    root.after(500, update_stats)  # update every 0.5s

# GUI setup
root = tk.Tk()
root.title("FPS & System Monitor")
root.configure(bg="black")

labels = {}
for key in ["FPS", "CPU", "RAM", "GPU Load", "GPU Temp", "GPU Mem"]:
    lbl = tk.Label(root, text=f"{key}: --", font=("Consolas", 12), fg="lime", bg="black")
    lbl.pack(anchor="w", padx=10, pady=2)
    labels[key] = lbl

frame_count = 0
start_time = time.time()

update_stats()
root.mainloop()
