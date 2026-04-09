from monitors.system_monitor import get_system_stats
from monitors.network_monitors import get_network_status
from config import HOSTS_TO_MONITOR


if __name__ == "__main__":
    system_stats = get_system_stats()
    network_stats = get_network_status(HOSTS_TO_MONITOR)

    print("SYSTEM STATS:")
    print(system_stats)

    print("\nNETWORK STATUS:")
    print(network_stats)