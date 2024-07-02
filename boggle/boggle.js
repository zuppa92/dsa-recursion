const boardString = `
N C A N E
O U I O P
Z Q Z O N
F A D P L
E D E A Z
`;

function makeBoard(boardString) {
    const rows = boardString.trim().split('\n');
    const board = rows.map(row => row.trim().split(' '));
    return board;
}

function isValidMove(board, x, y, visited) {
    return x >= 0 && x < 5 && y >= 0 && y < 5 && !visited.has(`${x},${y}`);
}

function searchWord(board, word, index, x, y, visited) {
    if (index === word.length) {
        return true;
    }

    if (!isValidMove(board, x, y, visited) || board[x][y] !== word[index]) {
        return false;
    }

    visited.add(`${x},${y}`);

    // Move in NEWS directions
    const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    for (const [dx, dy] of directions) {
        if (searchWord(board, word, index + 1, x + dx, y + dy, visited)) {
            return true;
        }
    }

    visited.delete(`${x},${y}`);
    return false;
}

function find(board, word) {
    for (let x = 0; x < 5; x++) {
        for (let y = 0; y < 5; y++) {
            if (searchWord(board, word, 0, x, y, new Set())) {
                return true;
            }
        }
    }
    return false;
}

function displayBoard(board) {
    const boardDiv = document.getElementById('boggle-board');
    boardDiv.innerHTML = '';
    board.forEach(row => {
        row.forEach(letter => {
            const cell = document.createElement('div');
            cell.textContent = letter;
            boardDiv.appendChild(cell);
        });
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const board = makeBoard(boardString);
    displayBoard(board);

    const checkButton = document.getElementById('check-word');
    const wordInput = document.getElementById('word-input');
    const message = document.getElementById('message');

    checkButton.addEventListener('click', () => {
        const word = wordInput.value.toUpperCase().trim();
        if (word && find(board, word)) {
            message.textContent = `"${word}" is found!`;
            message.style.color = 'green';
        } else {
            message.textContent = `"${word}" is not found.`;
            message.style.color = 'red';
        }
        wordInput.value = '';
    });
});
