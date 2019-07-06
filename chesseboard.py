import numpy as np
a = np.ones (64)
b = a.reshape (8,8)
print ("#######CHESSBOARD#######")
for i in range (0, 8):
    for j in range (0,8):
        if (i+j) % 2 == 0:
            b[i][j] = 0

print (b)
print ("#############################")
print ("Where you want to place the queen?")

row = int(input ("Enter row"))

column = int(input ("Enter column"))
print ("####################")
if row <8 and column<8:
    b[row-1] [column-1]=9
    print (b)
    print("QUEEN (9) has been placed!!")
    print( "#############")
else:
    print("invalid input")