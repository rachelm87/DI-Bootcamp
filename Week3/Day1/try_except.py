#Try and Except Block

# print('Hello World)

# move = int(input('Give ur move from 1 - 9: '))

      
while True:
    try:
        move = float(input('Give ur move from 1 - 9: '))
        move = round(move)
        if move < 1 or move > 9:
            raise Exception('Choose a number in range 1 - 9')
        
        print('thank you for the right input')
        break
    except Exception as e:
        print(e)
    finally:
        print('finally message')
    


