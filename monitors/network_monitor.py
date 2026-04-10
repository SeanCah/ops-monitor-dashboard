import socket
import subprocess
import platform


def ping_host(host):
    """
    Check if a host is reachable using ping.
    Returns True if reachable, False otherwise.
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    
    command = ["ping", param, "1", host]
    
    try:
        result = subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    except Exception:
        return False


def check_port(host, port):
    """
    Check if a specific port is open on a host.
    Returns True if open, False otherwise.
    """
    try:
        with socket.create_connection((host, port), timeout=2):
            return True
    except Exception:
        return False


def get_network_status(hosts):
    """
    Check multiple hosts and return their status.
    """
    results = []

    for host in hosts:
        status = {
            "host": host,
            "reachable": ping_host(host),
            "port_80_open": check_port(host, 80)
        }
        results.append(status)

    return results