# ServiceSentry

ServiceSentry is a Python-based utility designed to monitor and manage background services in Windows to prevent unnecessary resource usage. It helps optimize system performance by stopping services that are not critical to your operation.

## Features

- List all Windows services along with their current status.
- Stop unnecessary services to free up system resources.
- Start important services if they are accidentally stopped.
- Customizable list of important services that should always be running.
- Logging of service statuses and actions taken for auditing and troubleshooting.

## Installation

Ensure you have Python 3.x installed on your Windows machine. You also need to have `psutil` installed, which can be done via pip:
```bash
pip install psutil
```

## Usage

1. Clone the repository or download the `service_sentry.py` file.
2. Modify the `important_services` list in the script to include services that should not be stopped.
3. Run the script:
   ```bash
   python service_sentry.py
   ```

The script will continuously monitor your services every 120 seconds (or the interval you set) and take action to stop unnecessary ones.

## Configuration

- **check_interval**: The interval in seconds at which the services are checked (default is 60 seconds).
- **important_services**: A list of service names that should always remain running.

## Logging

ServiceSentry logs all actions and service statuses to `service_sentry.log`. This file can be used to review which services were stopped or started and when.

## Contributions

Contributions and pull requests are welcome. For any bug reports or feature requests, please create an issue on the GitHub repository.

## License

This project is licensed under the MIT License.