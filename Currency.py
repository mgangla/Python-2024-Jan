#Write a python program for a Currency Converter
#1 usd= 159.25 KES
#1 GBP= 203.32 KES
#1 ZAR= 8.56 KES

def ConverterCurr():
     numb = int(input("Enter amount in Dollars: "))
     Rate = 159.25
     value = numb * Rate
     print(numb, "is", value,"in Kenya Shillings")
ConverterCurr()



