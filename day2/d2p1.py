#! /usr/bin/env python3
# which game sets are possible if you have
# 12 red, 13 green, 14 blue
#Game 1: 20 green, 3 red, 2 blue; 9 red, 16 blue, 18 green; 6 blue, 19 red, 10 green
import re

def part_two(game_dict):
    total = 0
    
    for game in game_dict:
        print (f"\nGame {game}")
        print (f"{game_dict[game]}")
        green_max = 0
        red_max = 0
        blue_max = 0

        for hand in game_dict[game]:
            green = game_dict[game][hand].pop("green", "0")
            red = game_dict[game][hand].pop("red", "0")
            blue = game_dict[game][hand].pop("blue", "0")
            
            if int(green) > green_max:
                green_max = int(green)
            if int(red) > red_max:
                red_max = int(red)
            if int(blue) > blue_max:
                blue_max = int(blue)
        print (f"Green: {green_max}\nRed: {red_max}\nBlue: {blue_max}\n")
        total = total + (green_max * red_max * blue_max)
    
    print ("Part 2 Powers total: ", total)

def is_possible(game_dict): 
    total = 0
    
    for game in game_dict:
        possible = True
        #print (f"\nGame {game}")
        #print (f"{game_dict[game]}")

        for hand in game_dict[game]:
            green = game_dict[game][hand].pop("green", "0")
            red = game_dict[game][hand].pop("red", "0")
            blue = game_dict[game][hand].pop("blue", "0")
            #print("Popped: ", green)
            
            if int(green) > 13:
                possible = False
                break
            if int(red) > 12:
                possible = False
                break
            if int(blue) > 14:
                possible = False
                break

        if possible == True:
            #print ("WINNING GAME\n")
            total += int(game)
            # print ( int(game_dict[game][hand]['green']) )
    print (f"Part 1 total: {total}")

def main ():
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
    file_array = []
    game_dict = {}

    count = 0
    # Strips the newline character
    for line in Lines:
        file_array.append(line.strip())
        
    # Parse all the data into a dictionary
    for line in file_array:
        game = line.split(":")
        game_number = game[0]
        game_plays = game[1].split(";")
        
        # get the game number
        num = re.findall(r'\d+', game_number)
        # create a key for this game
        game_num = num[0]
        game_dict[game_num] = {}
        count = 0
        for hands in game_plays:
            this_hand = hands.split(",")
            #print(f"This hand: {this_hand}")
            game_dict[game_num]["hand_"+str(count)] = {}
            
            for draw in this_hand:
                num = draw.split()[0]
                color = draw.split()[1]
                game_dict[game_num]["hand_"+str(count)][color]=num
                #print (f"Color: {color} Number: {num}")
            count +=1           
        
    # Only run 1 or the other at a time
    # is_possible(game_dict)
    part_two(game_dict)

        
if __name__ == "__main__":
    main()
    