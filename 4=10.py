#problem: give n numbers, what combination of + - * / and () makes x
from itertools import permutations, product, zip_longest
from pars import genPars

def generate_permutations_and_operations(nums):
    perm = list(permutations(nums))
    ops = ['+', '-', '/', '*']
    allOps = product(ops, repeat=len(nums) - 1)
    
    all_combinations = []
    for p in perm:
        for o in allOps:
            combination = [str(p[0])]
            for i in range(1, len(p)):
                combination.append(o[i-1])
                combination.append(str(p[i]))
            all_combinations.append(''.join(combination))
    
    return all_combinations

def add_parentheses(combinations, num_count):
    parList = genPars(num_count)
    final_combinations = []
    
    for combination in combinations:
        final_combinations.append(combination)
        for p in parList:
            expr_with_parens = list(combination)
            if len(p) != 2:
                raise ValueError("Incorrect number of parentheses")
            expr_with_parens.insert(p[0], '(')
            expr_with_parens.insert(p[1] + 1, ')')
            final_combinations.append(''.join(expr_with_parens))
    
    return final_combinations

def evaluate_combinations(combinations, target):
    for expr in combinations:
        try:
            if eval(expr) == target:
                print(f"{expr} = {target}")
                return
        except ZeroDivisionError:
            continue
    
    print("No Solution")

def generate_all_number_combinations(n, m):
    return set([tuple(sorted(combination)) for combination in product(range(m), repeat=n)])

def main():
    all_number_combinations = generate_all_number_combinations(4, 10)
    
    for nums in all_number_combinations:
        expressions = generate_permutations_and_operations(nums)
        expressions_with_parens = add_parentheses(expressions, len(nums))
        evaluate_combinations(expressions_with_parens, 10)

if __name__ == "__main__":
    main()
