#write a python program to calculate the sum of numbers between 1 and a given number
#input the last number
num= int(input("Enter the last number: "))
def sumOfNum (num):
    sum1=0
    for i in range(1,num+1):
        sum1 = sum1+i
    print (sum1)
sumOfNum(num)
        