# suricata_controller.py

import subprocess

def start_suricata():
    try:
        # Adjust the path to suricata.yaml as per your actual path
        subprocess.run(["suricata", "-c", "C:\\Users\\user\\Desktop\\CodeAlpha\\CYBER SECURITY\\IPS_IDS\\suricata\\suricata.yaml", "-i", "wlan0", "-D"], check=True)
        return True, "Suricata started successfully"
    except subprocess.CalledProcessError as e:
        error_message = f"Error starting Suricata: {e}"
        print(error_message)
        return False, error_message

def stop_suricata():
    try:
        # Adjust the path to suricata.yaml and pidfile as per your actual path
        subprocess.run(["suricata", "-c", "C:\\Users\\user\\Desktop\\CodeAlpha\\CYBER SECURITY\\IPS_IDS\\suricata\\suricata.yaml", "--pidfile", "/var/run/suricata.pid", "-k", "shutdown"], check=True)
        return True, "Suricata stopped successfully"
    except subprocess.CalledProcessError as e:
        error_message = f"Error stopping Suricata: {e}"
        print(error_message)
        return False, error_message

def simulate_attack():
    try:
        return True, "Attack simulated successfully"
    except Exception as e:
        error_message = f"Error simulating attack: {e}"
        print(error_message)
        return False, error_message
