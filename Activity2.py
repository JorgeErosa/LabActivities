# 1. Write a function that takes two parameters, `num1` and `num2`, and returns their sum.
def sum_num(num1, num2):
    return(num1+num2)


# 2. Create a text file named "numbers.txt" and write a few numbers, each on a new line.
with open("numbers.txt", "w") as f:
    f.write("1\n2\n3\n4\n5")
    f.close()


# 3. Write a function that reads the numbers from the file and calculates their average.
def read_and_avg(file):    
    with open(file, "r") as f:
        numbers= f.readlines()
        f.close()

    count=0
    num_sum=0
    for num in numbers:
        count += 1
        num_sum+=int(num.strip())

    return(num_sum/count)


# 4. Implement a function that takes a string as input and writes it to the end of the "numbers.txt" file.
def add_string(string, file):
    with open(file, "a") as f:
        f.write("\n"+string)
        f.close()
    
    return(file)



# 5. Call the functions and print the results.
print(sum_num(5,10))
print(read_and_avg("numbers.txt"))
print(add_string("added string", "numbers.txt"))