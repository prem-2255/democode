let display = document.getElementById('display');
let currentNumber = '';
let previousNumber = '';
let operator = '';

function clearDisplay() {
    display.value = '';
    currentNumber = '';
    previousNumber = '';
    operator = '';
}

function backspace() {
    currentNumber = currentNumber.slice(0, -1);
    display.value = currentNumber;
}

function appendNumber(number) {
    currentNumber += number;
    display.value = currentNumber;
}

function appendOperator(op) {
    if (op === '=') {
        calculateResult();
    } else {
        previousNumber = currentNumber;
        currentNumber = '';
        operator = op;
    }
}

function calculateResult() {
    let result;
    switch (operator) {
        case '+':
            result = parseFloat(previousNumber) + parseFloat(currentNumber);
            break;
        case '-':
            result = parseFloat(previousNumber) - parseFloat(currentNumber);
            break;
        case '*':
            result = parseFloat(previousNumber) * parseFloat(currentNumber);
            break;
        case '/':
            result = parseFloat(previousNumber) / parseFloat(currentNumber);
            break;
        default:
            result = 0;
    }
    display.value = result;
    currentNumber = result.toString();
    previousNumber = '';
    operator = '';
}