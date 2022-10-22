# a teacher has given a task to susan . the task is that the teacher has an extremely large number with more than 
#5 digits. susan has to find the product of the first digit and the last digit of the provided number, and also she 
#has to check weather the result is divisible by 5 or not . if it is divisible by 5,she should respond with True 
#otherwise False. Susan finds it as difficult to answer can you help her to complete her task?
  
a = str(input(""))
b = int(a[0])*int(a[-1])
print(b)
if b%5 == 0: 
    print("True")
else:
    print("False")