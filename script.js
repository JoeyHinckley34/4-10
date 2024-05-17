// script.js

document.getElementById('expression-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const numbers = document.getElementById('numbers').value.split(',').map(Number);
    const target = Number(document.getElementById('target').value);
    const resultDiv = document.getElementById('result');

    const expression = findExpression(numbers, target);
    if (expression) {
        resultDiv.textContent = `Expression: ${expression} = ${target}`;
    } else {
        resultDiv.textContent = 'No valid expression found.';
    }
});

function evalExpression(expression) {
    try {
        return eval(expression);
    } catch {
        return null;
    }
}

function* generateExpressions(numbers) {
    if (numbers.length === 1) {
        yield numbers[0].toString();
    } else {
        for (let i = 0; i < numbers.length; i++) {
            const left = numbers[i];
            const rightNumbers = numbers.slice(0, i).concat(numbers.slice(i + 1));
            for (const subExpr of generateExpressions(rightNumbers)) {
                yield `(${left} + ${subExpr})`;
                yield `(${left} - ${subExpr})`;
                yield `(${left} * ${subExpr})`;
                if (subExpr !== "0") { // Avoid division by zero
                    yield `(${left} / ${subExpr})`;
                }
            }
        }
    }
}

function findExpression(numbers, target) {
    const permutations = permute(numbers);
    for (const perm of permutations) {
        for (const expr of generateExpressions(perm)) {
            if (evalExpression(expr) === target) {
                return expr;
            }
        }
    }
    return null;
}

function permute(nums) {
    if (nums.length === 0) return [[]];
    const result = [];
    for (let i = 0; i < nums.length; i++) {
        const rest = permute(nums.slice(0, i).concat(nums.slice(i + 1)));
        for (const subarray of rest) {
            result.push([nums[i], ...subarray]);
        }
    }
    return result;
}
