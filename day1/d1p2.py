#! /usr/bin/env python3
import re

def main ():


    # find the ints in the string
    # combine the ints into a string number
    # convert the string to an int
    # add the ints


    file1 = open('p1_input.txt','r')
    Lines = file1.readlines()
    string_array = []
    number_map = {
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9
    }
    
    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        string_array.append(line.strip())
      
    str_nums = []
    total = 0
    
    for string in string_array:
        num_str = ""
        word_num = ""
        pos_dict = {}
        iterator = 0
        
        
        for number in number_map:
            if number in string:
                # find all occurrences of this number
                if string.count(number) == 1:
                    pos_dict["num_"+ str(iterator)] = {}
                    pos_dict['num_'+ str(iterator)]["str"] = number
                    pos_dict['num_'+ str(iterator)]["position"] = string.find(number)
                    #print(number_map[number])
                    iterator += 1
                else:
                    res = [i.start() for i in re.finditer(number, string)]
                    for occur in res:
                        pos_dict["num_"+ str(iterator)] = {}
                        pos_dict['num_'+ str(iterator)]["str"] = number
                        pos_dict['num_'+ str(iterator)]["position"] = occur
                        iterator += 1


        for char in string:
            if char.isdigit():
                if string.count(char) == 1:
                    pos_dict["num_"+ str(iterator)] = {}
                    pos_dict['num_'+ str(iterator)]["integer"] = char
                    pos_dict['num_'+ str(iterator)]["position"] = string.find(char)
                    iterator += 1
                else:
                    # find all occurrences of this number
                    res = [i.start() for i in re.finditer(char, string)]
                    for occur in res:
                        pos_dict["num_"+ str(iterator)] = {}
                        pos_dict['num_'+ str(iterator)]["integer"] = char
                        pos_dict['num_'+ str(iterator)]["position"] = occur

                        iterator += 1

        
        lowest_pos = 1000
        highest_pos = 0
        lowest_num = 0
        highest_num = 0
        
        print ( f"String {string}")
        #print (pos_dict)
        
        for num in pos_dict:
            if pos_dict[num]['position'] <= lowest_pos:
                #print (f"[{pos_dict[num]['position']}] is lower than [{lowest_pos}]")
                try: 
                    integer = number_map[pos_dict[num]['str']]
                    #print (f"New most left STRING number: {int}")
                    #print(int)
                    lowest_num = integer
                    lowest_pos = pos_dict[num]['position']
                except: pass
                try:
                    integer = pos_dict[num]['integer']
                    #print (f"New most left INT number: {int}")
                    #print(int)
                    lowest_num = integer
                    lowest_pos = pos_dict[num]['position']
                except: pass
        
        for num in pos_dict:
            if pos_dict[num]['position'] >= highest_pos:
                #print (f"[{pos_dict[num]['position']}] is greater than [{highest_pos}]")
                try: 
                    integer = number_map[pos_dict[num]['str']]
                    #print (f"New most left STRING number: {int}")
                    #print(int)
                    highest_num = integer
                    highest_pos = pos_dict[num]['position']
                except: pass
                try:
                    integer = pos_dict[num]['integer']
                    #print (f"New most left INT number: {int}")
                    #print(int)
                    highest_num = integer
                    highest_pos = pos_dict[num]['position']
                except: pass
        
        if highest_pos == 0:
            print ("This string should have only one number")
            num_str += str(lowest_num)
            num_str += str(lowest_num)
        else:
            num_str += str(lowest_num)
            num_str += str(highest_num)
            
        print (f"Leftmost number: {lowest_num}")
        print (f"Rightmost number: {highest_num}")
        print (f"Combined numbers: {num_str} \n")
        
        total += int(num_str)
    
    print (f"Total: {total}")

if __name__ == "__main__":
    main()
    