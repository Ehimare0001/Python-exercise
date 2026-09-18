celcius = float(input("Enter temperature in celcius: "))

for count in range(5):
    current_temperature = celcius + count
    
    if current_temperature >= -273:
      
       fahrenheit = current_temperature * 9/5 + 32
      
       print(fahrenheit)
    else:
   
        print("impossible!")




