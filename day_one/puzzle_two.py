line_answers = []
with open("input.txt") as input_file:
    for line in input_file:
        line_answer = ""
        for char_index,char in enumerate(line):
            print(char_index)
            try:
                int(char)
            except:
                if "one" in line[char_index:char_index + 3].lower():
                    line_answer = f"{line_answer}1"
                elif "two" in line[char_index:char_index + 3].lower():
                    line_answer = f"{line_answer}2"
                elif "three" in line[char_index:char_index + 5].lower():
                    line_answer = f"{line_answer}3"
                elif "four" in line[char_index:char_index + 4].lower():
                    line_answer = f"{line_answer}4"
                elif "five" in line[char_index:char_index + 4].lower():
                    line_answer = f"{line_answer}5"
                elif "six" in line[char_index:char_index + 3].lower():
                    line_answer = f"{line_answer}6"
                elif "seven" in line[char_index:char_index + 5].lower():
                    line_answer = f"{line_answer}7"
                elif "eight" in line[char_index:char_index + 5].lower():
                    line_answer = f"{line_answer}8"
                elif "nine" in line[char_index:char_index + 4].lower():
                    line_answer = f"{line_answer}9"
            else:
                line_answer = f"{line_answer}{char}"    
        if len(line_answer) > 2:
            line_answer = f"{line_answer[0]}{line_answer[-1]}"
        if len(line_answer) == 1:
            line_answer = f"{line_answer}{line_answer}"
        line_answers.append(int(line_answer))
print(sum(line_answers))