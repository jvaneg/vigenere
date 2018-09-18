import sys

file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]

#read files as byte arrays (mutable)
f1Data = bytearray(open(file1,"rb").read())
f2Data = bytearray(open(file2,"rb").read())

#set output file to be length of shortest input file
if(len(f1Data) <= len(f2Data)):
    outSize = len(f1Data)
else:
    outSize = len(f2Data)

outData = bytearray(outSize)

# do the XOR
for index in range(outSize):
    outData[index] = f1Data[index] ^ f2Data[index]
    
# write the bytes to the output file

open(file3,"wb").write(outData)

print("Done")