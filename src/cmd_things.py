def cmd():
    input('Welcome to the Swamp 7 Terminal. Press enter to continue.')

    chose_text = False
    text = ""
    ceil = ""

    while True:
        op = input('Would you like to start rendering or add a floor and ceiling texture? (r/t)').lower()
        if op == 't':
            text = input('Input name of FLOOR texture (NOT CEILING): ')
            ceil = input('Input name of CEILING texture (NOT FLOOR): ')
            chose_text = True
            continue
        
        if op == 'r':
            if chose_text:
                return True, text, ceil
            else:
                print('You must provide a floor and ceiling texture!')
                continue
        

            

