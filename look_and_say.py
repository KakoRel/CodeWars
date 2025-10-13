"""""""""""""""
Your task is to create a function that will take an integer and return the result of the 
look-and-say function on that integer. This should be a general function that takes as 
input any positive integer, and returns an integer; inputs are not limited to the sequence 
which starts with "1".

Conway's Look-and-say sequence goes like this:

Start with a number.
Look at the number, and group consecutive digits together.
For each digit group, say the number of digits, then the digit itself.
This can be repeated on its result to generate the sequence.

For example:

Start with 1.
There is one 1 --> 11
Start with 11. There are two 1 digits --> 21
Start with 21. There is one 2 and one 1 --> 1211
Start with 1211. There is one 1, one 2, and two 1s --> 111221
"""""""""""""""

def look_say(num):
    digits = str(num)
    result = []
    
    i = 0
    while i < len(digits):
        count = 1
        current_digit = digits[i]
        
        while i + count < len(digits) and digits[i + count] == current_digit:
            count += 1
        
        result.append(str(count))
        result.append(current_digit)
        
        i += count
    
    return int(''.join(result))