# 1. Create a list of integers containing at least 10 elements
random_list=[1,20,50,43,2,64,18,21,44,72,91,5,16]

# 2. Write a function that takes the list as input and returns the maximum and minimum values.
def max_min_list(list):
    max=0
    min=100
    for i in range(len(list)):
        if list[i]< min:
            min=list[i]
        if list[i]> max:
            max=list[i]
    print("The maximum value of the list is {} and the minimum value is {}".format(max, min))
    return(min,max)

max_min_list(random_list)

# 3. Implement a function that reverses the order of the elements in the list.
def reverse_list(list):
    new_list=[]
    for i in list:
        new_list.insert(0,i)
    
    print("The original list was {} and the reversed list is {}".format(list, new_list))
    return(new_list)

reverse_list(random_list)

# 4. Write a function that searches for a given value in the list and returns its index.
def find_index(list, value):
    for i in range(len(list)):
        if list[i]==value:
            a=i

    print("The index of value {} is {}".format(value, a))
    return(a)

find_index(random_list, 44)

# 5. Implement a function that takes a list of numbers and returns a new list with only the even numbers.
def even_num(list):
    even_list=[]
    for i in range(len(list)):
        if list[i]%2 == 0:
            even_list.append(list[i])

    print("The original list was {} and the even numbered list is {}".format(list, even_list))
    return(even_list)

even_num(random_list)