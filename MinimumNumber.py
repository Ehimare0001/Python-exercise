numbers =[9, 43, 82, 2, 76, 12, 97, 45]

def minimum_number(numbers):
    smallest = numbers[0]
    
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest
    
print(minimum_number(numbers))
