import psutil
import wmi
import pynvml
import time
import os


# ---------- CPU USAGE & TEMP ----------
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


def get_cpu_temp():
    try:
        w = wmi.WMI(namespace="root\\wmi")
        temperature_info = w.MSAcpi_ThermalZoneTemperature()
        if temperature_info:
            # Convert from tenths of Kelvin to Celsius
            return round((temperature_info[0].CurrentTemperature / 10) - 273.15, 1)
    except Exception:
        pass
    return None  # Not available


# ---------- GPU USAGE & TEMP ----------
def get_gpu_info():
    try:
        pynvml.nvmlInit()
        handle = pynvml.nvmlDeviceGetHandleByIndex(0)

        name = pynvml.nvmlDeviceGetName(handle).decode()
        temp = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)

        util = pynvml.nvmlDeviceGetUtilizationRates(handle)
        gpu_util = util.gpu  # GPU usage %
        mem_util = util.memory  # Memory controller usage %

        pynvml.nvmlShutdown()

        return {
            "name": name,
            "temp": temp,
            "gpu_util": gpu_util,
            "mem_util": mem_util,
        }
    except Exception as e:
        return None


# ---------- MAIN LOOP ----------
if __name__ == "__main__":
    while True:
        os.system("cls")  # clear screen on Windows

        # CPU
        cpu_usage = get_cpu_usage()
        cpu_temp = get_cpu_temp()

        print("=== CPU ===")
        print(f"Usage: {cpu_usage:.1f}%")
        if cpu_temp is not None:
            print(f"Temperature: {cpu_temp} °C")
        else:
            print("Temperature: Not available (Windows limitation)")

        # GPU
        gpu = get_gpu_info()
        print("\n=== GPU ===")
        if gpu:
            print(f"Name: {gpu['name']}")
            print(f"Usage: {gpu['gpu_util']}%")
            print(f"Memory Controller: {gpu['mem_util']}%")
            print(f"Temperature: {gpu['temp']} °C")
        else:
            print("No NVIDIA GPU detected or NVML not installed")

        time.sleep(2)  # refresh every 2 seconds
