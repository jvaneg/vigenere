import sys

file1 = sys.argv[1]
file2 = sys.argv[2]
key = sys.argv[3]

#read files as byte arrays (mutable)
f1Data = bytearray(open(file1,"rb").read())
keyData = bytearray(key.encode())

#set output file to be length of the input file
outData = bytearray(len(f1Data))

# do the XOR
for index in range(len(f1Data)):
    outData[index] = f1Data[index] ^ keyData[index % len(keyData)]
    
# write the bytes to the output file

open(file2,"wb").write(outData)

print("Done")