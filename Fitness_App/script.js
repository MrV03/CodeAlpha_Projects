let workouts = [];

function addWorkout() {
    const sessionName = document.getElementById('workout-session-name').value.trim();
    if (!sessionName) {
        alert('Please enter a workout session name.');
        return;
    }

    const exercises = [];
    const exerciseFields = document.querySelectorAll('.exercise-field');
    exerciseFields.forEach(field => {
        const exerciseName = field.querySelector('.exercise-name').value.trim();
        const sets = parseInt(field.querySelector('.exercise-sets').value);
        const reps = parseInt(field.querySelector('.exercise-reps').value);
        const type = field.querySelector('.exercise-type').value;
        let weight = null;
        if (type === 'FW') {
            weight = parseFloat(field.querySelector('.exercise-weight').value);
        }
        exercises.push({ exerciseName, sets, reps, type, weight });
    });

    workouts.push({ sessionName, exercises });
    resetForm();
    displayWorkouts();
}

function resetForm() {
    document.getElementById('workout-session-name').value = '';
    document.getElementById('exercise-fields').innerHTML = `
        <div class="exercise-field">
            <input type="text" class="exercise-name" placeholder="Exercise Name">
            <input type="number" class="exercise-sets" placeholder="Sets">
            <input type="number" class="exercise-reps" placeholder="Reps">
            <select class="exercise-type">
                <option value="BW">BW (Bodyweight)</option>
                <option value="FW">FW (Free Weight)</option>
            </select>
            <input type="number" class="exercise-weight" placeholder="Weight (kg)" style="display:none;">
            <button class="add-exercise" onclick="addExerciseField()">Add Exercise</button>
        </div>
    `;
}

function displayWorkouts() {
    const workoutList = document.getElementById('workout-list');
    workoutList.innerHTML = '';
    workouts.forEach((workout, index) => {
        const li = document.createElement('li');
        li.innerHTML = `
            <h3>${workout.sessionName}</h3>
            <ul>
                ${workout.exercises.map(exercise => `
                    <li>
                        <span>Exercise:</span> ${exercise.exerciseName} <br>
                        <span>Sets:</span> ${exercise.sets} <br>
                        <span>Reps:</span> ${exercise.reps} <br>
                        <span>Type:</span> ${exercise.type === 'BW' ? 'Bodyweight' : 'Free Weight'} ${exercise.weight ? `(${exercise.weight} kg)` : ''} <br>
                    </li>
                `).join('')}
            </ul>
            <button onclick="deleteWorkout(${index})">Delete</button>
        `;
        li.classList.add('workout-item');
        workoutList.appendChild(li);
    });
}

function addExerciseField() {
    const exerciseFields = document.getElementById('exercise-fields');
    const div = document.createElement('div');
    div.classList.add('exercise-field');
    div.innerHTML = `
        <input type="text" class="exercise-name" placeholder="Exercise Name">
        <input type="number" class="exercise-sets" placeholder="Sets">
        <input type="number" class="exercise-reps" placeholder="Reps">
        <select class="exercise-type" onchange="toggleWeightInput(this)">
            <option value="BW">BW (Bodyweight)</option>
            <option value="FW">FW (Free Weight)</option>
        </select>
        <input type="number" class="exercise-weight" placeholder="Weight (kg)" style="display:none;">
        <button class="add-exercise" onclick="addExerciseField()">Add Exercise</button>
    `;
    exerciseFields.appendChild(div);
}

function toggleWeightInput(select) {
    const weightInput = select.parentElement.querySelector('.exercise-weight');
    if (select.value === 'FW') {
        weightInput.style.display = 'inline-block';
    } else {
        weightInput.style.display = 'none';
    }
}

function deleteWorkout(index) {
    workouts.splice(index, 1);
    displayWorkouts();
}
