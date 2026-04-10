from flask import Flask, render_template
from monitors.system_monitor import get_system_stats
from monitors.network_monitor import get_network_status
from config import HOSTS_TO_MONITOR
from utils.logger import setup_logger

app = Flask(__name__)
logger = setup_logger()


@app.route("/")
def dashboard():
    try:
        system_stats = get_system_stats()
        network_stats = get_network_status(HOSTS_TO_MONITOR)

        logger.info(f"System Stats: {system_stats}")
        logger.info(f"Network Status: {network_stats}")

        return render_template(
            "dashboard.html",
            system_stats=system_stats,
            network_stats=network_stats
        )

    except Exception as e:
        logger.error(f"Dashboard error: {str(e)}")
        return f"An error occurred: {str(e)}", 500


if __name__ == "__main__":
    app.run(debug=True)