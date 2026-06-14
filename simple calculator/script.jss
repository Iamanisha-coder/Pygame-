const display = document.getElementById('display');

function appendValue(val) {
    display.value += val;
}

function clearDisplay() {
    display.value = '';
}

function deleteLast() {
    display.value = display.value.slice(0, -1);
}

function calculate() {
    try {
        // eval handles basic string math execution safely for simple internal projects
        display.value = eval(display.value);
    } catch (error) {
        display.value = 'Error';
    }
}
