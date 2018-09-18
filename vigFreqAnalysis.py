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

    #print(characters)

    for (k,v) in characters.items():
        print(k + " - " + str(v))

    #if a third arg was added
    if(len(argv) > 3):
        #list of chars that likely correspond to E (this is very naive but will probably work on big enough inputs)
        #you should still manually inspect the frequency analysis to figure out the key        
        letterEList = [None] * keyLength
        letterEFreq = [0] * keyLength

        firstIteration = True

        for(k,v) in characters.items():
            if(firstIteration):
                firstIteration = False
                letterEFreq = v
                for i in range(0,len(letterEList)):
                    letterEList[i] = k
            else:
                for i in range(0,len(v)):
                    if(v[i] > letterEFreq[i]):
                        letterEList[i] = k
                        letterEFreq[i] = v[i]


        print("Most frequently occurring in each slot (likely to be letter E):")
        print(letterEList)
    
        eChar = 'E'
        eCharData = bytearray(eChar.encode())
        potentialKeyData = bytearray(("".join(letterEList)).encode())

        keyString = ""

        for byte in potentialKeyData:
            keyString += chr(eCharData[0] ^ byte)

        print("Using E as most common letter in alphabet")
        print("The key is most likely: " + keyString)
    

    
    
if __name__ == "__main__":
    main(sys.argv)