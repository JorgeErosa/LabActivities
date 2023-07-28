# 1. Declare two variables, `num1` and `num2`, and assign them with integer values.
print("Step 1")
num1, num2 = 2, 5
print("THe numbers are", num1, "and", num2)

# 2. Write a program that checks if `num1` is greater than `num2` and prints the result.
print("Step 2 & 3")
if num1 > num2:
    print("The first number is greater than the second")
# 3. Use an `if-else` statement to determine if the values of `num1` and `num2` are equal or not, and print an appropriate message.
elif num1==num2:
    print("The numbers are equal")
else:
    print("The second number is greater than the first")

# 4. Prompt the user to enter a number and store it in a variable.
print("Step 4")
user_number=int(input("Please enter a number: "))

print("Step 5 \n")
# 5. Use a loop to print all the numbers from 1 to the user-input number.
for i in range(1,user_number+1):
    print(i)
