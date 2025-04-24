import psutil
import speedtest
import time
from datetime import datetime

# 获取 CPU 使用率
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

# 获取内存使用情况
def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

# 获取磁盘 I/O 性能
def get_disk_io():
    disk = psutil.disk_io_counters()
    return disk.read_bytes, disk.write_bytes

# 网络带宽测试
def get_network_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # 转换为Mbps
    upload_speed = st.upload() / 1_000_000
    return download_speed, upload_speed

# 输出性能测试结果到日志文件
def log_performance():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    read_bytes, write_bytes = get_disk_io()
    download_speed, upload_speed = get_network_speed()

    log_message = f""" 
    Performance Test - {now}

    CPU Usage: {cpu_usage}%
    Memory Usage: {memory_usage}%
    Disk Read: {read_bytes / (1024 ** 2)} MB
    Disk Write: {write_bytes / (1024 ** 2)} MB
    Download Speed: {download_speed:.2f} Mbps
    Upload Speed: {upload_speed:.2f} Mbps
    """
    
    with open("performance_log.txt", "a") as f:
        f.write(log_message + "\n")
    print(log_message)

if __name__ == "__main__":
    log_performance()