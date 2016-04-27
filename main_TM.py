#Program by: Marcus Brumfield
#NETID: mib21

from turing_machine import *

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

    alphabet = infile.readline().strip().split()
    tape_alphabet = infile.readline().strip().split()

    sub = len(tape_alphabet) - 1
    blank = tape_alphabet[sub]

    states = infile.readline().strip().split()
    start_state = infile.readline().strip()
    accept_state = infile.readline().strip().split()
    reject_state = infile.readline().strip().split()

    while loop3:
        transition = infile.readline().strip()
        if transition == '':
            break
        else:
            add = transition
            rules.append(add.split())
            row += 1
        
    for r in range(row):
        for c in range(col):
            key1 = rules[r][0]
            key2 = rules[r][1]
            value1 = rules[r][2]
            value2 = rules[r][3]
            value3 = rules[r][4]
            key = (rules[r][0], rules[r][1])
            value = (rules[r][2], rules[r][3], rules[r][4])

            transition_function[key] = value
            
    infile.close()

    t = TuringMachine(tape = tape_input, blank_symbol = blank,
                      tape_alphabet = alphabet,
                      initial_state = start_state,
                      accepting_states = accept_state,
                      reject_states = reject_state, 
                      transition_function = transition_function)

    t.simulate()
    print('')
    loop1 = input('Do you want to start the Turing Machine simulator? (yes/no) ')
  
