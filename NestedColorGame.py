favorite_color = 'blue'

for count in range(3):
    guess = input('Guess the color: ')
    
    if guess==favorite_color:
        print('Corrected')
        break
        
    else:
        if guess == 'green':
            print('Closed')
            
        else:
            print('Wrong')
