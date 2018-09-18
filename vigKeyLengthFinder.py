import sys
from prime_math import get_factors

def main(argv):
    file1 = argv[1]

    #read file as string
    f1String = open(file1, "r").read()

    #substrings hashtable
    substrings = {}
    #repeated strings list
    repeatStrings = []

    for repeatLen in range(3,5):

        for i in range(0,len(f1String) - repeatLen + 1):
                substring = f1String[i:i+repeatLen]
                if((substring in substrings) and (i not in range(substrings[substring][0],substrings[substring][1]+1))):
                    spacing = i - substrings[substring][0]
                    repeatStrings.append((substring, spacing))
                    substrings[substring] = (i,i+repeatLen-1)
                else:
                    substrings[substring] = (i,i+repeatLen-1)
                
    #print(repeatStrings)            
    
    #factors of all spacing between repeat strings
    allFactors = {}
    
    
    #could optimize here by caching numbers ive already found the factors of
    for string in repeatStrings:
        factors = get_factors(string[1])
        #print(factors)
        for factor in factors:
            if(factor != 1):
                if(factor in allFactors):
                    allFactors[factor] += 1
                else:
                    allFactors[factor] = 1
                
    #print(allFactors)
    
    sortedFactors = sorted(list(allFactors.items()), key=lambda tup: tup[1], reverse=True)
    
    #print(sortedFactors)
    
    print("Top 5 most likely key lengths")
    print("1. " + str(sortedFactors[0][0]) + " characters long (factor appears " + str(sortedFactors[0][1]) + " times)")
    print("2. " + str(sortedFactors[1][0]) + " characters long (factor appears " + str(sortedFactors[1][1]) + " times)")
    print("3. " + str(sortedFactors[2][0]) + " characters long (factor appears " + str(sortedFactors[2][1]) + " times)")
    print("4. " + str(sortedFactors[3][0]) + " characters long (factor appears " + str(sortedFactors[3][1]) + " times)")
    print("5. " + str(sortedFactors[4][0]) + " characters long (factor appears " + str(sortedFactors[4][1]) + " times)")
        
    #print("Done")
    

    
    
if __name__ == "__main__":
    main(sys.argv)