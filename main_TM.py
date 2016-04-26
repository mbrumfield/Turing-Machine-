#Program by: Marcus Brumfield
#NETID: mib21

class TuringMachine:
    def __init__(self, 
                 tape, 
                 blank_symbol,
                 tape_alphabet,
                 initial_state,
                 accepting_states,
                 reject_states,
                 transition_function):
        self.__tape = list(tape)
        self.__head_position = 0
        self.__blank_symbol = blank_symbol
        self.__tape.append(self.__blank_symbol)
        self.__current_state = initial_state
        self.__acceptstate = accepting_states
        self.__transition_function = transition_function
        self.__tape_alphabet = tape_alphabet
        self.__reject_states = reject_states

    def __str__(self):
        s = ""
        s += 'Tape: ' + str(self.__tape)  + '\n' + 'Current: ' + self.__current_state + '\n'

        return s

    
    def simulate(self):
        count = 0
        tape = self.__tape
        size = len(list(tape))
        
        
        print('Should stop here: ', self.__acceptstate[0])
        print('')
        while self.__current_state != self.__acceptstate[0] and self.__current_state != self.__reject_states[0]:
            tape_print = ''
            current_read = self.__tape[count]
            tup = (self.__current_state, self.__tape[count])
            if tup in self.__transition_function.keys():
                print('Current state: ', self.__current_state)
                tape[count] = self.__transition_function[tup][1]
                
                self.__current_state = self.__transition_function[tup][0]
                
                for x in tape:
                    tape_print += x
                print('Tape: ', '\t\t', tape_print)
                print('Head: ', '\t\t', end='')
                for y in range(0, count):
                    print(' ', end='')
                print(' |')
                
                if self.__transition_function[tup][2] == 'L':
                    count -= 1
                elif self.__transition_function[tup][2] == 'R':
                    count += 1
                else:
                    print('Derp')
                    break
            else:
                print('Derp')
                break
        print('')
        print('Result: ')
        if self.__current_state == self.__acceptstate[0]:
            print('ACCEPT!')
        elif self.__current_state == self.__reject_states[0]:
            print('REJECT!')
        else:
            print('REJECT - There is an error in the tape.')
            
