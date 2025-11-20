print("=== Basic Calculator ===")
print("Please select from the following (1-4): ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

try:
  choice = int(input("Your Choice: "))

  if choice not in (1, 2, 3, 4):
      print("Invalid Choice. Please select a number between 1 and 4")
  else:
      num1 = float(input("First Number: "))
      num2 = float(input("Second Number: "))

      if choice == 1:
          print(f"{num1} + {num2} = {num1 + num2}")
      elif choice == 2:
          print(f"{num1} - {num2} = {num1 -num2}")
      elif choice == 3:
          print(f"{num1} * {num2} = {num1 * num2}")
      elif choice == 4:
          if num2 == 0:
              print("Error: Division by zero is Impossible")
          else:
              print(f"{num1} / {num2} = {num1 / num2}")

except ValueError:
    print("Invalid Input. enter numeric values only")
