#STR

#Write a paragraph on your identified domain. Write a python program
#to find the frequency of the given word(your domain name) in the paragraph.
a= """
Gym and club management systems provide fitness businesses the functionality to manage schedules, memberships, and facilities. 
The capabilities of gym management systems include storing member information in a database, managing the financial records,
 scheduling classes, and the reserving facilities."""
c=a.lower
print(a.count(c))

#to compute the number of characters, words and lines in the paragraph

#print(len(c))##number of characters
d=c.split()
print(len(d))#number of words
print(c.count("\n"))#number of lines

#to arrange the letters of the given word(your domain name) in alphabetical order

str="gymmanagement"
print(sorted(str))


##Write a python program to encrypt a given string(your domain name) using the following method:
##Encrypt Method: Add a number ‘n’(given by the user ) to each alphabet in the
##given string to create the corresponding letter

def enc(string, n):
 encrypted_string = "" 
 for char in string:
       if char.isalpha():
            is_uppercase = char.isupper()
            base = ord('A') if is_uppercase else ord('a')
            encrypted_char = chr((ord(char) - base + n) % 26 + base)
       else:
            encrypted_char = char

            encrypted_string += encrypted_char

 return encrypted_string


domain_name = input("Enter your domain name: ")
n = int(input("Enter the value of 'n': "))

encrypted_domain_name = enc(domain_name, n)
print("Encrypted domain name:", encrypted_domain_name)









 #2. Functions
 #Implement a function pay() that takes as input two arguments: an hourly wage and the number of hours an employee worked last week. Your function should compute and return the employee’s pay. Any hours worked beyond 40 is overtime and should be paid 1.5 times the regular hourly wage.
 #>>> pay(10,35)
 #350
 #>>>pay(10,45)
#475.0

a=int(input("Enter the hourly wage :"))
b=int(input(" Enter the number of hours worked :"))

def pay(a,b):

    c=min(40,b) ##regular hours
    d=max(0,b-40)  ##overtime hours

    e=c*a
    d=d*(a*1.5)

    Total_wage=e+d
    return Total_wage
Total_wage=pay(a,b) 
print(Total_wage)

#3. Tuple
#Create a list of tuples that consists of two neumatic and one string
#For example houses for rent, the number of bedrooms and their prices, like so:
#[ ('main st.', 4, 4000), ('elm st.', 1, 1200), ('pine st.', 2, 1600)]
#Sort the list in the following ways:
#In ascending order by first numeric value
#In descending order by second numeric value
#In alphabetical order of string value

item=[('rohit',2,800),('vinay',3,1000),('adharsh',1,1200)]

#In ascending order by first numeric value

item.sort(key=lambda x: x[1])
print(item)

#In descending order by second numeric value

item.sort(key=lambda x: x[2], reverse=True)
print(item)

#In alphabetical order of string value
item.sort(key=lambda x: x[0])
print(item)



 