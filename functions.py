

#Write a Python function that takes two arguments (a and b) and returns their sum.
def add_numbers(a,b):
    result =a+b
    return result
print(add_numbers(5,9))

#Write a Python function that takes a string as input and returns the string reversed.
def word(name):
    return name[::-1]
my_sentence=word("I love praying football")
print(my_sentence)    

#Write a Python function that takes a list of integers as input and returns the sum of all the integers in the list.

def addition(nums):
    sum=0
    for num in nums:
          sum=sum+1
    return sum
print(addition([4,6,8,9,3]))        



        
#Write a Python function that takes a list of integers as input and returns a new list with all the even numbers removed.
def remove_even_numbers(nums):
    empty=[]
    for value in nums:
        if value %2!=0:
            empty.append(value)
    return empty        
print(remove_even_numbers([10, 5, 7, 1]))            
        
#Write a Python function that takes a list of integers as input and returns the highest value in the list.
def highest_value(nums):
    highest=max(nums)
    return highest
   
print(highest_value([1,5,8,9,5,4])) 

#Write a Python function that takes a list of strings as input and returns a new list with all the strings capitalized.
def people_capitalize(name):
    capital=name.upper()
    return capital
print(people_capitalize("magdaline"))    



