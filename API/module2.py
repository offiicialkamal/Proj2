import math
import time 
# i fdo
def convert_to_binary(decimal):
    decimal_value = int(decimal)
    print(decimal_value)
    binary_list = []
    new_binary = None
    #now i have to convert it nto binary
    #while decimal_value > 1:
    
    while not decimal_value == 0 or decimal_value == 1: #AT THE SAME TIME BOTH ARE NOT GONNA TRUE OR FALSE BECAUSE VALUE WILL BE ONLY 0 OR ONE AT A TIME 
        new_binary = decimal_value % 2
        binary_list.append(new_binary)
        print(new_binary, decimal_value, sep=" ===>>>> ")

        #update the values for next loops
        new_binary = None
        decimal_value = math.floor(decimal_value / 2)
        time.sleep(2) # for better readability wait for 2 sconds
    

    bin = ""
    for binary in binary_list:
        bin = str(binary) + bin
        
    return bin
    