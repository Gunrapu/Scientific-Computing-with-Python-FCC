def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        raise ValueError('Error: Too many problems.')
    
    arranged_problems = [[], [], [], []]

    for problem in problems:
        operand_1, operator, operand_2 = problem.split();

        if operator not in ['+', '-']:
            raise ValueError("Error: Operator must be '+' or '-'.")
        if not operand_1.isdigit() or not operand_2.isdigit():
            raise ValueError('Error: Numbers must only contain digits.')
        if len(str(operand_1)) > 4 or len(str(operand_2)) > 4:
            raise ValueError('Error: Numbers cannot be more than four digits.')

        if operator == '+':
            answer = int(operand_1) + int(operand_2)
        else:
            answer = int(operand_1) - int(operand_2)

        max_length = max(len(str(operand_1)), len(str(operand_2)))

        line_1 = operand_1.rjust(max_length + 2)
        line_2 = f"{operator} {operand_2.rjust(max_length)}"
        line_3 = '-' * (max_length + 2)
        line_4 = f'{str(answer).rjust(max_length + 2)}'

        arranged_problems[0].append(line_1)
        arranged_problems[1].append(line_2)
        arranged_problems[2].append(line_3)
        arranged_problems[3].append(line_4)

        arranged_line = ["    ".join(lines) for lines in arranged_problems] 
        arranged_string = "\n".join(arranged_line)
    
    return arranged_string

try:
    print(arithmetic_arranger(["2 + 1", "1 - 2"]))
except ValueError as e:
    print(e)