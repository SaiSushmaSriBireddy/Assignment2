#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1.Write a program that takes two strings from the user: first_name, last_name. Pass these variables to
#fullname function that should return the (full name).

first_name=input("enter  first name:")
#taking first name from the user
last_name=input("enter last name:")
#taking last name from the user
full_name=(first_name+' '+last_name)
#combining both first and last name 
print(full_name)
# Here we  print full name


#-Write function named “string_alternative” that returns every other char in the full_name string.

def string_alternative(str):#creating a function
    result=""#taking a new string
    for i in range (len(str)):#range of function
        if(i%2==0):#if condition to print alternate charaters
           result+=str[i] #adding alternate characters to the new string
    return result#return the new string
print(string_alternative("Good Morning"))#calling the function in the main function


#2.Write a python program to find the wordcount in a file (input.txt) for each line and then print the output.
#o Finally store the output in output.txt file. 

input_file = open('input.txt', 'r')#reading the input file
count = dict()# to count 
source = input_file.read()# read data from the input file
words = source.split()# splitting the words
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(count)
f = open('output.txt', 'w')#writing the output file
f.write(source)
f.write('\nword_count:\n')
for key, value in count.items():
    f.write(f"{key}: {value}\n")
f.close()


#3.Write a program, which reads heights (inches.) of customers into a list and convert these
#heights to centimeters in a separate list using:

list_inches=list(map(float,input('enter list').split()))#input list in inches
list_cm=[]#new list in cm
for i in list_inches:
    i*=2.54#convertion
    list_cm.append(i)
print(list_cm)  #printion  



# In[ ]:





# In[ ]:




