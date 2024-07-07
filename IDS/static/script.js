// script.js

document.addEventListener('DOMContentLoaded', () => {
    getStatus();
});

function getStatus() {
    fetch('/get_suricata_status')
        .then(response => response.json())
        .then(data => {
            document.getElementById('status').textContent = data.status;
        });
}

function startSuricata() {
    fetch('/start_suricata')
        .then(response => response.json())
        .then(data => {
            document.getElementById('status').textContent = data.message;
        });
}

function simulateAttack() {
    fetch('/simulate_attack')
        .then(response => response.json())
        .then(data => {
            document.getElementById('attack-log').textContent = data.message;
            document.getElementById('attack-details').textContent = data.details;
        });
}

function stopSuricata() {
    fetch('/stop_suricata')
        .then(response => response.json())
        .then(data => {
            document.getElementById('status').textContent = data.message;
        });
}
