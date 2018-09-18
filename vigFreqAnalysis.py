import sys
from prime_math import get_factors

def main(argv):
    file1 = argv[1]
    keyLength = int(argv[2])

    #read file as string
    f1String = open(file1, "r").read()

    #characters hashtable
    characters = {}

    for i in range(0,len(f1String)):
        char = f1String[i]
        if(f1String[i] in characters):
            characters[char][i % keyLength] += 1
        else:
            freqList = [0] * keyLength
            characters[char] = freqList
            characters[char][i % keyLength] += 1

    print(characters)
                          
    
    
    print("Done")
    

    
    
if __name__ == "__main__":
    main(sys.argv)