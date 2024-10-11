
import numpy as np
import pandas as pd

#################################### 8.32 ####################################

def Simpletron_v2(file):
    print("""*** Welcome to Simpletron! ***
    *** Please enter your program one instruction ***
    *** ( or data word ) at a time into the input ***
    *** text field. I will display the location ***
    *** number and a question mark (?). You then ***
    *** type the word for that location. Enter ***
    *** -99999 to stop entering your program. ***""")
    handle = open(file,'r')
    idx = 0
    memory = [0] * 100
    for line in handle:
        memory[idx] = (int(line))
        idx += 1
    
    instructionCounter = 0
    accumulator = 0
    while True:
        instructionRegister = memory[instructionCounter]
        operationCode = instructionRegister // 100
        operand = instructionRegister % 100

        while instructionRegister != -99999 and (instructionRegister > 9999 or instructionRegister < -9999):
            print('Enter a valid number -9999~9999')
            memory[instructionCounter] = int(input(str(instructionCounter) + ' ? '))
            instructionRegister = memory[instructionCounter]
        #operation execution
        if instructionRegister == -99999:
            print("""*** Program loading completed ***
                 *** Program execution begins ***""")
            return
        
        if operationCode == 10:
            word = int(input('enter a word:'))
            memory[operand] = word
            print(f'saved to location {operand}')
        elif operationCode == 11:
            print(f'print word in location {operand}')
            print(memory[operand])
        elif operationCode == 20:
            accumulator = int(memory[operand])
            print(f'loaded location {operand} into accumulator')
        elif operationCode == 21:
            memory[operand] = accumulator
            print(f'store accumulator in location {operand}')
        elif operationCode == 30:
            accumulator += memory[operand]
            print(f'add word from location {operand} to accumulator')
        elif operationCode == 31:
            accumulator -= memory[operand]
            print(f'subtract word from location {operand} from accumulator')
        elif operationCode == 32:
            if memory[operand] == 0:
                print('*** Attempt to divide by zero ***')
                print('*** Simpletron execution abnormally terminated ***')
                return
            else:
                accumulator /= memory[operand]
                print(f'divide word from location {operand} into the word accumulator')
        elif operationCode == 33:
            accumulator *= memory[operand]
            print(f'multiply a word from location {operand} by the word accumulator')
        elif operationCode == 40:
            operationCode = operand
            print(f'branch to location {operand}')
            continue
        elif operationCode == 41:
            if accumulator < 0:
                operationCode = operand
                print(f'The accumulator is negative, branch to location {operand}')
                continue
            else:
                print('accumulator is positive, move to next memory location')
        elif operationCode == 42:
            if accumulator == 0:
                operationCode = operand
                print(f'The accumulator is zero, branch to location {operand}')
                continue
            else:
                print('accumulator is not zero, move to next memory location')
        elif operationCode == 43:
            print(f"""REGISTERS:
        accumulator {accumulator}
        instructionCounter {instructionCounter}
        instructionRegister {instructionRegister}
        operationCode {operationCode}
        operand {operand}""")
            df = pd.Series(memory)
            df = df.values.reshape((10,10))
            df = pd.DataFrame(df, columns = range(0, 10), index = range(0, 100, 10))
            print('MEMORY:')
            print(df)
       
        instructionCounter += 1

        
###test
Simpletron_v2('data_input.txt')
