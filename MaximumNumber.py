numbers =[9, 43, 82, 2, 76, 12, 97, 134]

def maximum_number(numbers):

    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number
    return largest
    
print(maximum_number(numbers))
            
        
        
        

