# FPS & System Monitor (Python)

A simple **free and open-source system monitor** built with Python.  
It shows **FPS, CPU usage, RAM usage, GPU load, temperature, and memory** in a small live-updating window.  

This version uses **Tkinter** (built into Python), so no extra GUI libraries are required.

---

## ✨ Features
- ✅ Live FPS counter  
- ✅ CPU usage (%)  
- ✅ RAM usage (GB + %)  
- ✅ GPU load (%)  
- ✅ GPU temperature (°C)  
- ✅ GPU memory usage  

---

## 🖼️ Preview
The program opens a small floating window like this:



---

## ⚙️ Installation

1. Install Python **3.8+** (Windows/Linux/Mac).  
   [Download Python here](https://www.python.org/downloads/)

2. Clone this repository or download the script.

3. Install required Python libraries:

```bash
pip install psutil gputil nvidia-ml-py3
python monitor.py