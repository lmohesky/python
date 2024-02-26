# Author: Lance Mohesky
# For testing and benchmarking purposes only! Do not use this for malicious intent.

# Be sure to install psutil beforehand 'pip install psutil'
import psutil
import time

def increase_cpu_usage(duration_seconds):
    try:
        # Get the number of logical CPUs
        num_cpus = psutil.cpu_count(logical=True)

        # Create a list of CPU usage percentages for each CPU
        cpu_percentages = [100] * num_cpus

        # Start the CPU stress test
        with psutil.Popen(["stress-ng", "--cpu", str(num_cpus), "--cpu-load", "10", "--timeout", str(duration_seconds)]) as stress_process:
            # Monitor CPU usage during the test
            start_time = time.time()
            while time.time() - start_time < duration_seconds:
                cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
                print(f"Current CPU usage: {cpu_percent}")
                time.sleep(1)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_duration = 600  # 10 minutes
    increase_cpu_usage(test_duration)
