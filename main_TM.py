#Program by: Marcus Brumfield
#NETID: mib21

from test import *

loop1 = True
loop2 = True
loop3 = True

loop1 = input('Do you want to start the Turing Machine simulator? (yes/no) ')
while loop1:
    rules = []
    final = []
    row = 0
    col = 5
    transition_function = dict()
    
    if loop1.lower() == 'n' or loop1.lower() == 'no':
        break
    file_name = input("Enter the Turing Machine's file name. ")

    while loop2:
        try:
            infile = open(file_name, 'r')
            print('Turing Machine from ', file_name, ':')
            print('')
            break
        
        except:
            print('An error occured. ')
            file_name = input("Enter the Turing Machine's file name. ")

    tape_input = input('Enter Tape input: ')
    tape_input.split()

    ##file_contents = infile.read()
    ##print(file_contents)

    alphabet = infile.readline().strip().split()
    ##print('Input Alphabet: ', alphabet)
    tape_alphabet = infile.readline().strip().split()
    ##print('Tape Alphabet: ', tape_alphabet)

    sub = len(tape_alphabet) - 1
    blank = tape_alphabet[sub]
    ##print('Blank symbol = ', blank)

    states = infile.readline().strip().split()
    ##print('List of States: ', states)
    start_state = infile.readline().strip()
    ##print('Start State: ', start_state)
    accept_state = infile.readline().strip().split()
    ##print('Accept state: ', accept_state)
    reject_state = infile.readline().strip().split()
    ##print('Reject State: ', reject_state)

    ##for count in accept_state:
    ##    final.append(count)
    ##for count in reject_state:
    ##    final.append(count)
    ##print("Final: ", final)
          
    while loop3:
        transition = infile.readline().strip()
        #print(transition)
        if transition == '':
            break
        else:
            add = transition
            rules.append(add.split())
            row += 1
        

    ##print('Transition Rules: ')
    for r in range(row):
        for c in range(col):
            key1 = rules[r][0]
            key2 = rules[r][1]
            value1 = rules[r][2]
            value2 = rules[r][3]
            value3 = rules[r][4]
            key = (rules[r][0], rules[r][1])
            value = (rules[r][2], rules[r][3], rules[r][4])
            
    ##        print(key)
    ##        print(value)

            transition_function[key] = value
            
    ##print(transition_function)
    infile.close()

    t = TuringMachine(tape = tape_input, blank_symbol = blank,
                      tape_alphabet = alphabet,
                      initial_state = start_state,
                      accepting_states = accept_state,
                      reject_states = reject_state, 
                      transition_function = transition_function)
    ##print(t)
    t.simulate()
    print('')
    loop1 = input('Do you want to start the Turing Machine simulator? (yes/no) ')
    ##print("Input on Tape:")
    ##t.show_tape()
    ##while not t.final():
    ##    t.step()
    ##
    ##print("Result of the Turing machine calculation:")    
    ##t.show_tape()

    ##print('')

    ##Printing rules list
    ##for count in rules:
    ##    key = rules[count]
    ##    print(key)
    ##    print('')

    ##print(rules[0])
    ##print('')
    ##print('')
    ##print('')
    ##print(rules)
