from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Global variable to track Suricata status
suricata_running = False

# Route to render the index.html template
@app.route('/')
def index():
    return render_template('index.html')

# Route to start Suricata
@app.route('/start_suricata')
def start_suricata():
    global suricata_running
    suricata_running = True
    app.logger.info('Suricata started.')
    return jsonify({'message': 'Suricata started.'})

# Route to simulate an attack
@app.route('/simulate_attack')
def simulate_attack():
    global suricata_running
    if not suricata_running:
        return jsonify({'message': 'Suricata is not running. Please start Suricata to simulate an attack.'})

    # Logic to simulate different types of attacks randomly
    import random
    attacks = [
        {'type': 'DoS Attack', 'details': 'Denial of Service attack detected.'},
        {'type': 'Trojan Horse', 'details': 'Trojan Horse attack detected.'},
        {'type': 'Unauthorized Access', 'details': 'Unauthorized Access detected.'}
    ]
    attack = random.choice(attacks)
    app.logger.warning(f'Simulated {attack["type"]} attack: {attack["details"]}')
    return jsonify({'message': f'Simulated {attack["type"]} attack.', 'details': attack['details']})

# Route to stop Suricata
@app.route('/stop_suricata')
def stop_suricata():
    global suricata_running
    suricata_running = False
    app.logger.info('Suricata stopped.')
    return jsonify({'message': 'Suricata stopped.'})

# Route to get Suricata status
@app.route('/get_suricata_status')
def get_suricata_status():
    global suricata_running
    status = 'Suricata is running.' if suricata_running else 'Suricata is stopped.'
    return jsonify({'status': status})

if __name__ == '__main__':
    app.run(debug=True)
