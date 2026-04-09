import psutil


def get_cpu_usage():
    """
    Return current CPU usage as a percentage.
    """
    cpu_percent = psutil.cpu_percent(interval=1)
    return cpu_percent


def get_memory_usage():
    """
    Return memory usage details.
    """
    memory = psutil.virtual_memory()
    return {
        "total": memory.total,
        "used": memory.used,
        "percent": memory.percent
    }


def get_disk_usage():
    """
    Return disk usage details for the root drive.
    """
    disk = psutil.disk_usage("/")
    return {
        "total": disk.total,
        "used": disk.used,
        "percent": disk.percent
    }


def get_system_stats():
    """
    Return all collected system statistics in one dictionary.
    """
    return {
        "cpu": get_cpu_usage(),
        "memory": get_memory_usage(),
        "disk": get_disk_usage()
    }