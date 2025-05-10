import psutil
import time
import os

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    mem = psutil.virtual_memory()
    return mem.percent, mem.total, mem.used, mem.available

def main():
    os.system('clear')
    print("Monitoring CPU and Memory Usage\n")
    
    try:
        while True:
            cpu = get_cpu_usage()
            mem_percent, mem_total, mem_used, mem_avail = get_memory_usage()

            print(f"CPU Usage     : {cpu:.2f}%")
            print(f"Memory Usage  : {mem_percent:.2f}%")
            print(f"Total Memory  : {mem_total / (1024 ** 3):.2f} GB")
            print(f"Used Memory   : {mem_used / (1024 ** 3):.2f} GB")
            print(f"Available Mem : {mem_avail / (1024 ** 3):.2f} GB")
            print("-" * 40)

            time.sleep(3)
            os.system('clear')

    except KeyboardInterrupt:
        print("\nExiting monitoring...")

if __name__ == "__main__":
    main()
