while True:
   try:
       lower = int(input("Введіть нижню межу діапазону: "))
       upper = int(input("Введіть верхню межу діапазону: "))
       if lower <= 0 or upper <= 0:
           print("Будь ласка, введіть числа більше за 0.")
       else:
           break
   except ValueError:
       print("Будь ласка, введіть коректні числа.")
prime_numbers = []


for num in range(lower, upper + 1):
   if num > 1:
       is_prime = True
       for i in range(2, num):
           if num % i == 0:
               is_prime = False
               break
       if is_prime:
           prime_numbers.append(num)
if prime_numbers:
   print("Прості числа в заданому діапазоні:", prime_numbers)
else:
   print("Простих чисел в заданому діапазоні немає.")
