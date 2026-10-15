from collections import Counter
import re

LOG_FILE = "logs/sample_logs.txt"
FAILED_THRESHOLD = 3


def extract_ip(line):
    match = re.search(r"from (\d{1,3}(?:\.\d{1,3}){3})", line)
    return match.group(1) if match else None


def analyze_logs():
    failed_attempts = Counter()
    successful_logins = []

    with open(LOG_FILE, "r", encoding="utf-8") as file:
        for line in file:
            ip = extract_ip(line)

            if "Failed password" in line and ip:
                failed_attempts[ip] += 1

            elif "Accepted password" in line and ip:
                successful_logins.append((ip, line.strip()))

    print("=== SSH LOG ANALYSIS ===\n")

    print("Failed authentication attempts:")
    for ip, attempts in failed_attempts.items():
        status = "SUSPICIOUS" if attempts >= FAILED_THRESHOLD else "Monitor"
        print(f"{ip}: {attempts} attempts - {status}")

    print("\nSuccessful logins:")
    if successful_logins:
        for ip, event in successful_logins:
            print(f"{ip}: {event}")
    else:
        print("No successful logins detected.")


if __name__ == "__main__":
    analyze_logs()
