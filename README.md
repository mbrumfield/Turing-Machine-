# Turing-Machine

This is a Turing Machine simulator, in this case a single tape deterministic Turing machine. The program reads a file that describes a Turing Machine and then ask repeatedly for input words that is then determines if are or are not in the language.

The format for the TM is:
 
Line 1: The input alphabet. Tokens are separated by spaces
 
Line 2: The tape alphabet, including a designated ”blank” character. It must include the input alphabet as well.
 
Line 3: A list of states
 
Line 4: The start state
 
Line 5: The accept state
 
Line 6: The reject state
 
Line 7...n: Transition function rules of the form: State Input New State Output Direction. Separated by spaces
