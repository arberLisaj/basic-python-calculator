
def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def devide(x, y):
    return x / y


print("Choose your operator:")
print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")

while True:
   
    choice = input("Choose:(1/2/3/4): ")

   
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Insert the first Number: "))
        num2 = float(input("Insert the second Number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", substract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", devide(num1, num2))
            
# simple commment 
        next_calculation = input("Do you want to continue?  (yes/no): ")
        if next_calculation == "no":

          break
    

    # print out the value 
    else:
        print("Invalid Input")  