line_answers = []
with open("input.txt") as input_file:
    for line in input_file:
        line_answer = ""
        for char in line:
            try:
                int(char)
            except:
                pass
            else:
                line_answer = f"{line_answer}{char}"    
        if len(line_answer) > 2:
            line_answer = f"{line_answer[0]}{line_answer[-1]}"
        if len(line_answer) == 1:
            line_answer = f"{line_answer}{line_answer}"
        line_answers.append(int(line_answer))
print(sum(line_answers))