powers = []
with open("input.txt") as input:
    for line in input:
        line = line.strip()
        line = line.split(":")
        game_id = int(line[0].split("Game ")[1])
        pulls = line[1].split(";")
        high_red = 0
        high_green = 0
        high_blue = 0
        for pull in pulls:
            pull_loop = pull.split(",")
            
            for color in pull_loop:
                if "red" in color:
                    red_num = int(color.strip(" red"))
                    if red_num > high_red:
                        high_red = red_num
                if "green" in color:
                    green_num = int(color.strip(" green"))
                    if green_num > high_green:
                        high_green = green_num
                if "blue" in color:
                    blue_num = int(color.strip(" blue"))
                    if blue_num > high_blue:
                        high_blue = blue_num
        set_power = high_red * high_green * high_blue
        print(set_power)
        powers.append(set_power)
print(sum(powers))
            

                    