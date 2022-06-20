#這邊有帶入關於如何透過 True/False 來控制主程式進入迴圈狀態，讓程式可以循換運作
#我可能沒有想到的部分就是，我可以透過 While loop 搭配 True False 協助讓使用者選擇要繼續執行程式，還是要結束程式

import art

def sub(a,b):
  return a+b

def ext(a,b):
  return a-b

def mul(a,b):
  return a*b

def div(a,b):
  return a/b

def calculator():
  print(art.logo)
  
  first_num=float(input("What's the first number? "))
  keep_continue=True
  
  while keep_continue:
    print("+\n-\n*\n/")
    ops=input("Pick an operation: ")
    second_num=float(input("What's the next number?: "))

    if (ops=="+"):
      answer=sub(first_num,second_num)
      print(f"{first_num} + {second_num} = {answer}")
    elif (ops=="-"):
      answer=ext(first_num,second_num)
      print(f"{first_num} - {second_num} = {answer}")
    elif (ops=="*"):
      answer=mul(first_num,second_num)
      print(f"{first_num} * {second_num} = {answer}")
    elif (ops=="/"):
      answer=div(first_num,second_num)
      print(f"{first_num} / {second_num} = {answer}")
    
    choice=input("Type 'Y' to continue calculating with {answer}, or type 'N' to start a new calculation: ")
    if choice=="Y":
      first_num=answer
    elif choice=="N":
      keep_continue=False
      calculator()

calculator()
