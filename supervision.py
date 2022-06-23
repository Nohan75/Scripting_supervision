import os
import time

import psutil


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


functions = [log_cpu, log_memory, log_disk, log_network, log_sensors, log_other, log_processes]
