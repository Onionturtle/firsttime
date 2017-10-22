print("""Hello my friend!!
This is the Standard Deviation Calculator
Type in how many numbers you want to calculate.
Then put int the numbers.
""")
# theirinput = input()
# while theirinput is a number
# add the number to list
# if it is not an integer end the loop and print out to they again

the_list = list()
num = input()
num = int(num)

while(num > 0):
    num -= 1
    list_items = input()
    the_list.append(list_items)


print(the_list)
