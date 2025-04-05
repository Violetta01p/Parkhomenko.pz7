while True:
   try:
       start_sum = float(input("Enter the initial deposit amount: "))
       percent = float(input("Enter the annual interest rate (e.g., 5 for 5%): "))
       target_sum = float(input("Enter the desired final amount: "))
       if start_sum > 0 and percent > 0 and target_sum > 0:
           break
       else:
           print("All numbers must be greater than 0.")
   except ValueError:
       print("Please enter valid numbers.")


year = 0
current_sum = start_sum
while current_sum < target_sum:
   year += 1
   current_sum += current_sum * (percent / 100)
   print("Year " + str(year) + ": deposit amount = " + str(round(current_sum, 2)))


print("It will take " + str(year) + " years to reach at least " + str(target_sum) + ".")
