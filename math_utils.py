def find_max_number(num1, num2, num3):
    if (num1>num2) :
      if (num1>num3):
        return num1
      else
        return num3
    else
     if(num2>num3):
        return num2
num1 = 1
num2 = 3
num3 = -1
max_num = find_max_number(num1, num2, num3)
print("The maximum number is:", max_num)
