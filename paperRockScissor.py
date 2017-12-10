# Mike Bland
# Paper, Rock Scissor game
#

y = ['P','R','S']

x = input('Make your choice(P, R, S): (q to quit)')

if x != 'q' and x in y:
    while (x != 'q') and x in y:

        from random import *
             
        z = randint(0, 2)

        if x == 'P':
            human = 0
                
        if x == 'R':
            human = 1

        if x == 'S':
            human = 2


        if human == z:
            result = 'tie'


        if z == 0:
            if human == 1:
                result = 'computer'

        if z == 0:
            if human == 2:
                result = 'human'

        if z == 1:
            if human == 0:
                result = 'human'

        if z == 1:
            if human == 2:
                result = 'computer'

        if z == 2:
            if human == 0:
                result = 'computer'

        if z == 2:
            if human == 1:
                result = 'human'
                    
                
        print ('Human:', x,' ', 'Computer:',y[z])
        print ('winner is:', result)
            
        x = input('Make your choice: (q to quit)')

print('Good bye')

    
    
        


    



