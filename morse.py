from time import sleep

def translate_word(letter):
    if letter == "a" or letter == "A":
        letter = ".-"
    elif letter == "b" or letter == "B":
        letter = "-..."
    elif letter == "c" or letter == "C":
        letter = "-.-."
    elif letter == "d" or letter == "D":
        letter = "-.."
    elif letter == "e" or letter == "E":
        letter = "."
    elif letter == "f" or letter == "F":
        letter = "..-"
    elif letter == "g" or letter == "G":
        letter = "--"
    elif letter == "h" or letter == "H":
        letter = "...."
    elif letter == "i" or letter == "I":
        letter = ".."
    elif letter == "j" or letter == "J":
        letter = ".---"
    elif letter == "k" or letter == "K":
        letter = "-.-"
    elif letter == "l" or letter == "L":
        letter = ".-.."
    elif letter == "m" or letter == "M":
        letter = "--"
    elif letter == "n" or letter == "N":
        letter = "-."
    elif letter == "o" or letter == "O":
        letter = "---"
    elif letter == "p" or letter == "P":
        letter = ".--"
    elif letter == "q" or letter == "Q":
        letter = "--.-"
    elif letter == "r" or letter == "R":
        letter = ".-."
    elif letter == "s" or letter == "S":
        letter = "..."
    elif letter == "t" or letter == "T":
        letter = "-"
    elif letter == "u" or letter == "U":
        letter = "..-"
    elif letter == "v" or letter == "V":
        letter = "...-"
    elif letter == "w" or letter == "W":
        letter = ".--"
    elif letter == "x" or letter == "X":
        letter = "-..-"
    elif letter == "y" or letter == "Y":
        letter = "-.--"
    elif letter == "z" or letter == "Z":
        letter = "--.."
    elif letter == "1":
        letter = ".----"
    elif letter == "2":
        letter = "..---"
    elif letter == "3":
        letter = "...--"
    elif letter == "4":
        letter = "....-"
    elif letter == "5":
        letter = "....."
    elif letter == "6":
        letter = "-...."
    elif letter == "7":
        letter = "--..."
    elif letter == "8":
        letter = "---.."
    elif letter == "9":
        letter = "----."
    elif letter == "0":
        letter = "-----"
    elif letter == ",":
        letter = "--..--"
    elif letter == ".":
        letter = ".-.-.-"
    elif letter == "?":
        letter = "..--.."
    elif letter == "/":
        letter = "-..-."
    elif letter == "-":
        letter = "-....-"
    elif letter == "(":
        letter = "-.--."
    elif letter == ")":
        letter = "-.--.-"
    
    return letter
    
def main(): 
    word = list(input("Enter a word or phrase ('*' to quit): "))
    
    while word != ["*"]:
    
        new_word = word
    
        for i in range(len(word)):
            new_word[i] = translate_word(word[i])
    
        s = " "
    
        s = s.join(new_word)
    
        print(s)
    
        sleep(1)
        
        word = list(input("Enter a word or phrase ('*' to quit): "))
    
main()