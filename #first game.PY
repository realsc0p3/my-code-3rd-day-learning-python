
#My own fun paper game.py
def game(): #I have created a def function for my game, i feel like it is easier:

    color_picks = ('red', 'green', 'blue', 'yellow')
    number_picks = (1, 2, 3, 4, 5, 6, 7, 8)
    udsagn = {
          1: 'You are a rose',
          2: 'You are a sun',
          3: 'You are a star',
          4: 'You are a moon',
          5: 'You are a cloud',
          6: 'You are a rainbow', 
          7: 'You are a snowflake',
          8: 'You are a firefly'
    }

    print('Thank you for participating in my fun paper game, let us get started!')
    print('Are you ready to play? Type yes or no!')

    svar = input('yes/no: ')

    while svar != 'yes' and svar != 'no':
                print('That is not a valid response, try again!')
                svar = input('yes/no: ')

    print('We will start when you are ready!')

    picked_color = input('Choose a color between (red, green, blue, yellow): ')
    while picked_color not in color_picks:
        print('That is an invalid color, try again!')
        picked_color = input('Choose a color between (red, green, blue, yellow): ')

    print('You have chosen the color:', picked_color, 'and now you need to choose a number between 1 and 8!')

    
    while True:
          try:
                picked_number = int(input('Choose a number between 1 and 8: '))
                if 1 <= picked_number <= 8:
                      break
                else:
                        print('That is not a valid number, try again!')
          except ValueError:
                print('That is not a valid number, try again!')
    
    while picked_number not in number_picks:
        print('That is an invalid number, try again!')
        picked_number = int(input('Choose a number between 1 and 8: '))

    print('You have chosen the number:', picked_number, 'and the color:', picked_color, 'let us see what it says about you!')

    print('It says', udsagn[picked_number])
game() #Call the game function to start the game




    
    

    
