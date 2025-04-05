while True:
   try:
       number = int(input("Введіть ціле число для обчислення факторіала: "))
       if number < 0:
           print("Число повинно бути більшим або рівним 0.")
       else:
           break
   except ValueError:
       print("Будь ласка, введіть коректне ціле число.")
factorial = 1
multiplication_process = ""


i = 1
while i <= number:
   factorial *= i
   if multiplication_process == "":
       multiplication_process += str(i)
   else:
       multiplication_process += "*" + str(i)
   i += 1
print(f"{multiplication_process} = {factorial}")
