const SECRET_MIN = 1;
const SECRET_MAX = 50;
const MAX_TURNS = 7;

let secret = 0;
let turns = 0;
const guessInput = document.getElementById("guess-input");
const guessButton = document.getElementById("guess-button");
const restartButton = document.getElementById("restart-button");
const statusBox = document.getElementById("status");
const historyBox = document.getElementById("history");

function resetGame() {
    secret = Math.floor(Math.random() * (SECRET_MAX - SECRET_MIN + 1)) + SECRET_MIN;
    turns = 0;
    guessInput.value = "";
    guessInput.disabled = false;
    guessButton.disabled = false;
    statusBox.textContent = "Make your first guess!";
    historyBox.textContent = "";
    guessInput.focus();
}

function recordHistory(message) {
    historyBox.textContent += `\n${message}`;
}

function handleGuess() {
    const value = Number(guessInput.value);
    if (!Number.isInteger(value) || value < SECRET_MIN || value > SECRET_MAX) {
        statusBox.textContent = `Enter a whole number between ${SECRET_MIN} and ${SECRET_MAX}.`;
        return;
    }
    turns += 1;
    if (value === secret) {
        statusBox.textContent = `Correct! You guessed the number in ${turns} turn(s).`;
        guessInput.disabled = true;
        guessButton.disabled = true;
        recordHistory(`Turn ${turns}: ${value} (correct)`);
        return;
    }
    if (turns >= MAX_TURNS) {
        statusBox.textContent = `Out of turns! The number was ${secret}.`;
        guessInput.disabled = true;
        guessButton.disabled = true;
        recordHistory(`Turn ${turns}: ${value} (last guess)`);
        return;
    }
    if (value < secret) {
        statusBox.textContent = `Too low! Attempts left: ${MAX_TURNS - turns}.`;
        recordHistory(`Turn ${turns}: ${value} (low)`);
    } else {
        statusBox.textContent = `Too high! Attempts left: ${MAX_TURNS - turns}.`;
        recordHistory(`Turn ${turns}: ${value} (high)`);
    }
    guessInput.value = "";
    guessInput.focus();
}

guessButton.addEventListener("click", handleGuess);
restartButton.addEventListener("click", resetGame);
guessInput.addEventListener("keyup", (event) => {
    if (event.key === "Enter") {
        handleGuess();
    }
});

resetGame();
