import psutil
import subprocess
import time
import logging

class ServiceSentry:
    def __init__(self, check_interval=60):
        self.check_interval = check_interval
        self.important_services = []  # Add service names that are important and shouldn't be stopped
        logging.basicConfig(filename='service_sentry.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def list_services(self):
        """Lists all services with their status."""
        services = {service.name(): service.status() for service in psutil.win_service_iter()}
        for service, status in services.items():
            logging.info(f"Service: {service}, Status: {status}")
        return services

    def stop_service(self, service_name):
        """Stops a specific service."""
        try:
            subprocess.run(['net', 'stop', service_name], check=True)
            logging.info(f"Successfully stopped service: {service_name}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to stop service {service_name}: {e}")

    def start_service(self, service_name):
        """Starts a specific service."""
        try:
            subprocess.run(['net', 'start', service_name], check=True)
            logging.info(f"Successfully started service: {service_name}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to start service {service_name}: {e}")

    def monitor_services(self):
        """Monitors services and stops any unnecessary ones."""
        while True:
            services = self.list_services()
            for service, status in services.items():
                if service not in self.important_services and status == 'running':
                    logging.info(f"Stopping unnecessary service: {service}")
                    self.stop_service(service)
            time.sleep(self.check_interval)

if __name__ == "__main__":
    sentry = ServiceSentry(check_interval=120)
    sentry.important_services = ['WinDefend', 'W32Time']  # Example important services
    sentry.monitor_services()