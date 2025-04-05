import random
number_to_guess = random.randint(1, 100)
max_attempts = 7
print("Вгадайте число від 1 до 100! У вас є 7 спроб.")


for attempt in range(1, max_attempts + 1):
   user_guess = int(input(f"Спроба {attempt}: Введіть число: "))
   if user_guess == number_to_guess:
       print(f"Вітаємо! Ви вгадали число за {attempt} спроб!")
       break
   elif user_guess < number_to_guess:
       print("Загадане число більше.")
   else:
       print("Загадане число менше.")
   if attempt == max_attempts:
       print(f"Ви не вгадали число. Правильне число було {number_to_guess}.")
