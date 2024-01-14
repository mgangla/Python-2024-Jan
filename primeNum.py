#write a python program to determine prime numbers between 1 and a given number
def primesOfn(num):
    for j in range (1,num):
         if j>1:
            for i in range (2,j):
                if j % i ==0:
                    break
            else:
                print (j,"is a Prime")
primesOfn(31)
