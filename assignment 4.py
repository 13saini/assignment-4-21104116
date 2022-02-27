#QUESTION1
def hanoi(n,X,Z,Y):
    if n == 0:
        return
    hanoi(n-1,X,Y,Z)
    print ("move",n,"from", X, "to",Z)
    hanoi(n-1,Y,Z,X)
hanoi(3,'x','y','z')

#QUESTION2
print(" ")
# input rows
n = int(input("Enter the number of rows in Pascal's Triangle: "))

# using recursions
print("\nUsing recursions:\n")


def pascal(n, originaln=n):
    if n == 0:
        return

    pascal(n - 1, originaln)

    # printing the spaces
    print('  ' * (originaln - n), end='')

    # first number is always 1
    entry = 1
    for i in range(1, n + 1):
        print(entry, end='   ')

        # using Binomial Coefficient
        entry = entry * (n - i) // i
    print()


pascal(n)

# using ITERATIVE method
print("\nUsing Iterative method:\n")
for line in range(1, n + 1):

    # everything else same as recursion
    print('  ' * (n - line), end='')

    x = 1
    for i in range(1, line + 1):
        print(x, end='   ')

        x = x * (line - i) // i
    print()
print("")

#QUESTION3
def fun(a,b):
    divmod(a,b)
    return divmod(a,b)
num1 = int(input("enter first no. "))
num2 = int(input("enter second no. "))
a = fun(num1,num2)

#inbuilt function to find if the function is callable
print("answer 'a'")
print("print true if the function is callable ",callable(fun(4,2)))

print("answer 'b'")
print("print true if all values are non zero ",bool(0 not in a))

print("Answer 'c'")
b = a + (4,5,6)
print("unfiltered : ",b)

#inbuilt function to filter 
c = filter(lambda x: x<=4, b)
print("filtered tuple: ",tuple(c))

d = filter(lambda x: x<=4, b)

print("answer 'd'")
e = set(d)
print("converted into set data type : ",e)

print("answer 'e'")
f = frozenset(e) #makes set immutable
print("immutable set",f)

print("answer f")
print("maximum value in the set : ",max(f))
print("Hash value of the max value : ",hash(max(f)))

#QUESTION4
print(" ")


class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid

    def __del__(self):
        print("Object destroyed")


# creating object
student1 = Student("Harsh", 21104116)
print("Object created")

# printing the assigned values
print(f"The name of the student it {student1.name} and SID is {student1.sid}.")

# deleting object
del student1
print("")

#QUESTION5
class Employee():
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary
    def details(self):
        print(self.name ,  self.salary)


employee1 = Employee("Mehak" , 40000)
employee2 = Employee("Ashok" , 50000)
employee3 = Employee("Viren" , 60000)

print("NAME  SALARY")
employee1.details()
employee2.details()
employee3.details()

print("\nupdating details of mehak... ")

print("updated details of mehak :")
print("NAME  SALARY")
employee1.salary = 70000
employee1.details()

del employee3

#QUESTION6
print(" ")
# inputting a word from the first friend
word = input("Enter the first word: ")

# inputting a meaningful word with the exact same letters
testword = input("\nEnter a new meaningful word to test your friendship: ")


# defining dictionary from last assignment
def count_in_dict(word):
    count = {}
    list1 = list(word)

    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count


# test to verify the letters of the new word
if count_in_dict(word) != count_in_dict(testword):
    print("The letters aren't exact, friendship is fake!!")


# shopkeeper's input to verify the word's meaning
def userinput():
    ans = input("\nDoes the word makes sense?(y or n)\n")

    if ans == 'y':
        print("The friends pass the friendship test!!\n\n")
    elif ans == 'n':
        print("The word doesn't have a meaning, friendship is fake!!\n\n")
    else:
        print("Invalid input, try again")
        userinput()


userinput()
print("")
