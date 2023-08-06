import re
import sys


def main():
    #get user input as a list of individual letters
    ex_letters = re.findall(r'[a-z]', input("Excluded letters: "), re.IGNORECASE)
    in_letters = re.findall(r'[a-z]',input("Included letters: "), re.IGNORECASE)
    
    #existence and duplicate check
    if not in_letters and not ex_letters:
        print('No usable input')
        sys.exit(1)
    if duplicate(in_letters, ex_letters):
        print('Duplicate entries found')
        sys.exit(2)

    exact = None
    if in_letters:
        while True:
            choice = input('Specify exact positions?[y/n] ')
            if choice.lower() in ['y', 'n']:
                if choice.lower() == 'y':
                    #exact gets a tuple from pattern3 function
                    exact = pattern3(in_letters)
                    break
                else:
                    break
            else:
                print('Invalid answer')
    with open('dict.txt', encoding = 'utf-8') as file:
        for line in file:
            #first level, include 5 letter words without excluded letters
            if re.search(pattern1(ex_letters), line):
                #second level look for words with the included letters
                if re.search(pattern2(in_letters), line):
                    #third level, if exact locations exist, further narrow down results
                    if exact:
                        if re.search(exact[0], line):
                            if re.search(exact[1], line):
                                print(line.strip().upper())
                    else:
                        print(line.strip().upper())


#prevents execution if duplicates are found between included and excluded letters groups
def duplicate(group1, group2):
    for i, _ in enumerate(group1):
        for j, _ in enumerate(group2):
            if group1[i] == group2[j]:
                return True
    return False


#returns exclusion and length regex pattern
def pattern1(match):
    seq = ''
    for element in match:
        for c in element:
            seq += c
    #equence of type r'\b[^abcd..]{5}\b'
    return r'\b[^' + seq + r']{5}\b'


#returns inclusion regex pattern
def pattern2(match):
    seq = ''
    for element in match:
        for c in element:
            seq += r'(?=\w*' + c + r')'
    #sequence of type r'\b(?=w*a)(?=w*b)...\w+\b'
    return r'\b' + seq + r'\w+\b'


#returns positional regex pattern tuple
def pattern3(match):
    #create 2 dictionaries to store positional information
    #positions only stores one number per letter, exact positions
    positions = {i:'_' for i in range(5)}
    #not_positions stores a list of numbers for each letter, NOT positions 
    not_positions = {i:list() for i in range(5)}
    for element in match:
        for c in element:
            while True:
                #for exact positions, only one number is accepted
                n = input(f"Enter position of letter '{c.upper()}' (or leave empty and press enter): ")
                if n:
                    #check if in range and valid
                    try:
                        n = int(n)
                        if n in range(1,6):
                            positions[n - 1] = c
                            #break after successful assignment of exact position, since NOT position is not required in this case
                            break
                        else:
                            print('Valid positions: 1-5')
                            continue
                    except ValueError:
                        print('Valid positions: 1-5')
                        continue
                #if exact position was not given, request NOT position as a list of valid numbers
                np = re.findall(r'[1-5]', input(f"Enter NOT position(s) of letter '{c.upper()}' (or leave empty and press enter): "))
                if np:
                    #assign letter to each of it' s ΝΟΤ positions in the not_positions dictionary of list items
                    for number in np:
                        not_positions[int(number) - 1].append(c)
                    break
                if not n and not np:
                    break     
    #create each sequence
    seq_is = r'\b'
    seq_not = r'\b'
    for key in positions.keys():
        if positions[key] == '_':
            seq_is += r'\w{1}'
        else:
            seq_is += positions[key]
        if not_positions[key]:
            seq_not += r'[^'
            for n in not_positions[key]:
                seq_not += n
            seq_not += r']'
        else:
            seq_not += r'[a-z]'
    seq_is += r'\b'
    seq_not += r'\b'
    return seq_is, seq_not


if __name__ == '__main__':
    main()
