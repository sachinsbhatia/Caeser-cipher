alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

inpu= input("enter a string:")

lengthh= len(inpu)

outp= ""

for i in range(lengthh):
    character = inpu[i]
    char_loc = alpha.find(character)
    new_loc = char_loc + 3;
    outp += alpha[new_loc]


print("encrypted text is:", outp)
