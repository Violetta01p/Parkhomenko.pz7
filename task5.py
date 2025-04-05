bacteria = 10
growth_rate = 0.20
while True:
   try:
       max_bacteria = int(input("Введіть максимальну кількість бактерій: "))
       if max_bacteria <= bacteria:
           print("Максимальна кількість повинна бути більшою за 10.")
       else:
           break
   except ValueError:
       print("Будь ласка, введіть коректне ціле число.")
hours = 0
while bacteria < max_bacteria:
   hours += 1
   bacteria += bacteria * growth_rate  
   print("Година", hours, ":", int(bacteria), "бактерій")


print("Процес досягнув максимальної кількості бактерій за", hours, "годин.")
