#! /usr/bin/env python3

def main ():


    # find the ints in the string
    # combine the ints into a string number
    # convert the string to an int
    # add the ints


    file1 = open('p1_input.txt', 'r')
    Lines = file1.readlines()
    string_array = []
    
    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        string_array.append(line.strip())
      
    str_nums = []
    
    for string in string_array:
        x = ""
        for char in string:
            if char.isdigit():
                x += char
        print (int(x))
        str_nums.append(x)

    two_digit_nums = []
    total = 0

    for num in str_nums:
        y = ""
        y += num[0]
        y += num[len(num)-1]
        print (y)
        total += int(y)
    
    print (f"Total: {total}")

if __name__ == "__main__":
    main()
    