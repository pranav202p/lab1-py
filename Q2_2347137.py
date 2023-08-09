#Is the given list divisible by 3 or NOT?
list1=[8,6,3,10,9]
a=[x for x in list1 if x%3==0]
print(a)




#Square of even numbers in a list
list2=[10,5,2,8,6]
b=[x**2 for x in list2 if x%2==0]
print(b)




#Sum of digits of all EVEN numbers in a list
list3=[5,4,2,10,15]
c=sum([x for x in list3 if x%2==0])
print(c)



#Remove duplicate numbers in a list
list4 = [2,2,4,4,6,6,8,8]
d = list(set(list4))
print(d)


#2. Dictionary
#Create a dictionary to store the details of your company employees (name as key and
#birthdate as value).
#{ ‘Virat Kohli’: ‘5 November 1988’, ‘Umesh Yadav’: ‘25 October 1987’, ‘Manish Pandey’:
#‘10 September 1989’, ‘Rohit Sharma’: ‘30 April 1987’, ‘Ravindra Jadeja’: ‘6 December
#1988’, ‘Hardik Pandya’: ‘11 October 1993’ }
#Write a function birthDate() that takes the full name of your employees(as a string) and
#displays the given employee’s birthdate.
#>>>birthDate(‘Rohit Sharma’)
#‘30 April 1987’

employee_details = {
    'Virat Kohli': '5 November 1988',
    'Umesh Yadav': '25 October 1987',
    'Manish Pandey': '10 September 1989',
    'Rohit Sharma': '30 April 1987',
    'Ravindra Jadeja': '6 December 1988',
    'Hardik Pandya': '11 October 1993'
}

def birthDate(full_name):
    if full_name in employee_details:
        return employee_details[full_name]
    else:
        return "Employee not found."

# Test the function
employee_name = "Rohit Sharma"
birthdate = birthDate(employee_name)
print(f"{employee_name}'s birthdate is: {birthdate}")

