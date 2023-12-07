red_max = 12
green_max = 13
blue_max = 14
possible_games = []
with open("input.txt") as input:
    for line in input:
        line = line.strip()
        line = line.split(":")
        game_id = int(line[0].split("Game ")[1])
        pulls = line[1].split(";")
        pull_pass = True
        for pull in pulls:
            pull_loop = pull.split(",")
            
            for color in pull_loop:
                if "red" in color:
                    red_num = int(color.strip(" red"))
                    if red_num > red_max:
                        pull_pass = False
                if "green" in color:
                    green_num = int(color.strip(" green"))
                    if green_num > green_max:
                        pull_pass = False
                if "blue" in color:
                    blue_num = int(color.strip(" blue"))
                    if blue_num > blue_max:
                        pull_pass = False
        if pull_pass:
            possible_games.append(game_id)
    print(sum(possible_games))
                    