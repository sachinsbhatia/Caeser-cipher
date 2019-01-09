alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

inpu= input("enter a string:")

shift_input= int(input("Enter in the value you want to shift by:"))
 
lengthh= len(inpu)

outp= ""

for i in range(lengthh):
    character = inpu[i]
    char_loc = alpha.find(character)
    new_loc = (char_loc + shift_input)%26;
    outp = outp + alpha[new_loc]


print("encrypted text is:", outp)
