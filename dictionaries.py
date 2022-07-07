# Write a program in Python to remove duplicate items from a list.
def remove_duplicates():
   lista=[1,2,2,2,2,2,3,3,3,3,4,5,6,7,8]
   empty_list=[]
      
   for i in lista:

        if i not in empty_list:
            empty_list.append(i)
   print(empty_list)
remove_duplicates()

lista=[1,2,2,2,2,2,3,3,3,3,4,5,6,7,8]
empty_listb=[]
[empty_listb.append(x) for x in lista if x not in empty_listb]
print(empty_listb)





# Q2. Write a program, to sum up, all the elements of a list.
def sum_list():
    listd=[10,2]

    sum=0
    # for i in listd:
    #     sum+=i
    #     i+=1
    b=[]
    [sum:=sum+i for i in listd]
    
    print(sum)
sum_list()

# Q3. Write a program to sum all the values of a dictionary.

# Q4. Use a dictionary to store antonyms of words. E.g.- 'Right':'Left', 'Up':'Down', etc. Display all words and then ask the user to enter a word and display the antonym of it.
# Q5: Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are squares of keys.
# Q6: Write a Python program to create a dictionary from two lists without losing duplicate values.
# Q7: Write a Python program to convert more than one list to a nested dictionary.
# Q8. Write a Python program to change the position of every n-th value with the (n+1)th in a list.
# Q9: Write a Python program to move all zero digits to the end of a given list of numbers.e
#    Ie; Original_list=[1,30,2,0,4,21,0,45,23,78,0,12,0,5]
#          Expected_Outcome=[1,30,2,4,21,45,23,78,12,5,0,0,0,0]
# Q10: Write a Python program to remove consecutive duplicates of a given list.
# Q11: Write a Python program to check whether an element exists within a tuple.
# Q12: Write a Python program to convert a given string list to a tuple.

  #create a dictionary of values of integers
#create a default variable of zero
#loop through values of the dictionary 
#assign it to the variable
#print the variable
dict_2={"Bluebird":45,"android":6,"Book":45}
starting=0
for i in dict_2.values():
    starting+=i
print(starting)
  #create a function,
  #cerate a dictionary of words with their opposites 
  #request user for a word
  #condition the request if it is in key print value of the dictionary 
  #print value of the specific key
def opposite():
    ask=str(input("Enter a word, "))
    dict_opp={"Right":"Left","Bottom":"Up","Top":"Bottom"}
    if ask in dict_opp.keys():
        print(f"{dict_opp[ask]} is the opposite of {ask}")
    else:
        return ask
opposite()
# Q5: Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are squares of keys.
def dicting_val():
    dict1={"people":5,"Laptops":5,"books":4}
    sum2=0
    p=list(dict1.values())
    [sum2:=sum2+i for i in p]
    print(sum2)
dicting_val()
def looping(n):
    dicta={}
    for i in range(1,n+1):
        dicta[i]=i*i
    print(dicta)
looping(15)






