let flashcards = [];
let currentCardIndex = 0;
let score = 0;

function addFlashcard() {
    const question = document.getElementById('new-question').value;
    const answer = document.getElementById('new-answer').value;
    if (question && answer) {
        flashcards.push({ question, answer });
        document.getElementById('new-question').value = '';
        document.getElementById('new-answer').value = '';
    }
}

function quizMe() {
    if (flashcards.length === 0) {
        alert('Please add some flashcards first.');
        return;
    }

    currentCardIndex = Math.floor(Math.random() * flashcards.length);
    showFlashcard(currentCardIndex);
}

function showFlashcard(index) {
    const flashcard = flashcards[index];
    document.getElementById('question').innerText = flashcard.question;
    document.getElementById('answer').innerText = flashcard.answer;
    document.getElementById('answer').style.display = 'none';
    document.getElementById('feedback-buttons').style.display = 'none'; // Hide feedback buttons initially
}

function revealAnswer() {
    document.getElementById('answer').style.display = 'block';
    document.getElementById('feedback-buttons').style.display = 'block'; // Show feedback buttons after revealing answer
}

function updateScore(isCorrect) {
    if (isCorrect) {
        score++;
    }
    document.getElementById('score').innerText = 'Score: ' + score;
    document.getElementById('feedback-buttons').style.display = 'none'; // Hide feedback buttons after scoring
}

// Initial function call to show first flashcard
if (flashcards.length > 0) {
    showFlashcard(currentCardIndex);
}
