import datetime
import os
import time

import psutil


# data = "testdata,data=cpu number=8"
now = datetime.datetime.now()


def send_cpu():
    """
    Send CPU data
    :return: CPU data as list
    """
    # CPU
    print("   > CPU ")
    cpu_time = 'cpu,data=cpu cpu_time=' + str(psutil.cpu_times()[0])
    percent = 'cpu,data=cpu percent=' + str(psutil.cpu_percent())
    count = 'cpu,data=cpu count=' + str(psutil.cpu_count())
    time_percent = 'cpu,data=cpu time_percent=' + str(psutil.cpu_times_percent(percpu=False).user)
    frequency = 'cpu,data=cpu frequency=' + str(psutil.cpu_freq().current)
    load_avg = 'cpu,data=cpu load_avg=' + str(psutil.getloadavg()[0])
    return [cpu_time, percent, count, time_percent, frequency, load_avg]


def send_memory():
    """
    Send memory data
    :return: memory data as list
    """
    # Memory
    print("   > Memory ")
    memory = "memory,data=memory virtual=" + str(psutil.virtual_memory().total)
    swap = "memory,data=memory swap=" + str(psutil.swap_memory().total)
    process = "memory,data=memory process=" + str(psutil.Process(os.getpid()).memory_info().rss)
    return [memory, swap, process]


def send_disk():
    """
    Send disk data
    :return: Disk data as list
    """
    # Disk
    print("   > Disk ")
    usage = "disk,data=disk usage=" + str(psutil.disk_usage('/').total)
    return [usage]


def send_network():
    """
    Send network data
    :return: Network data as list
    """
    # Network
    print("   > Network ")
    counters = "network,data=network io counters=" + str(psutil.net_io_counters(pernic=True))
    stats = "network,data=network net stats=" + str(psutil.net_if_stats())
    address = "network,data=network net if address=" + str(psutil.net_if_addrs())
    return [counters, stats, address]


def send_sensors():
    """
    Send sensors data
    :return: Sensors data as list
    """
    # Sensors
    print("   > Sensors ")
    battery = "sensors,data=sensors battery=" + str(psutil.sensors_battery().percent)
    return [battery]


def send_other():
    """
    Send other data
    :return: some other data as list
    """
    # Other
    print("   > Other")
    boot = "other,data=boot boot_time=" + str(psutil.boot_time())
    return [boot]


def send_all():
    """
    Send all data as list of function
    :return: functions as list
    """
    # Send all data
    print(" >>> Send all data: ")
    return [send_cpu(), send_memory(), send_disk(), send_sensors(), send_other()]


def log_cpu():
    # CPU
    print(" --- CPU --- ")
    print("cpu time: " + str(psutil.cpu_times()))
    print("cpu percent: " + str(psutil.cpu_percent()))
    print("cpu count: " + str(psutil.cpu_count()) + " cores")
    print("cpu time percent: " + str(psutil.cpu_times_percent(percpu=False)))
    print("cpu stats: " + str(psutil.cpu_stats()))
    print("cpu frequency: " + str(psutil.cpu_freq()))
    print("cpu load avg: " + str(psutil.getloadavg()))


def log_memory():
    # Memory
    print("\n")
    print(" --- Memory --- ")
    print("memory virtual: " + str(psutil.virtual_memory()))
    print("memory swap: " + str(psutil.swap_memory()))
    print("memory process: " + str(psutil.Process(os.getpid()).memory_info()))


def log_disk():
    # Disk
    print("\n")
    print(" --- Disk --- ")
    print("disk partitions: " + str(psutil.disk_partitions()))
    print("disk usage: " + str(psutil.disk_usage('/')))
    print("disk io counters: " + str(psutil.disk_io_counters()))
    print("disk io counters per disk: " + str(psutil.disk_io_counters(perdisk=True)))


def log_network():
    # Network
    print("\n")
    print(" --- Network --- ")
    print("network io counters: " + str(psutil.net_io_counters(pernic=True)))
    print("network net stats: " + str(psutil.net_if_stats()))
    print("network net if address: " + str(psutil.net_if_addrs()))


def log_sensors():
    # Sensors
    print("\n")
    print(" --- Sensors --- ")
    print("sensors battery: " + str(psutil.sensors_battery()))


def log_other():
    # Other
    print("\n")
    print(" --- Other --- ")
    print("boot time: " + str(psutil.boot_time()) + " seconds")
    print("users: " + str(psutil.users()))


def log_processes():
    # Processes management
    print("\n")
    print(" --- Processes management --- ")
    print("pids: " + str(psutil.pids()))
    p = psutil.Process(os.getpid())
    print("process: " + str(p))
    print("process name: " + str(p.name()))
    print("process exe: " + str(p.exe()))
