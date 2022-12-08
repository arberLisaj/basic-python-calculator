
def mbledhje(x, y):
    return x + y

def zbritje(x, y):
    return x - y

def shumzim(x, y):
    return x * y

def pjestim(x, y):
    return x / y


print("Zgjidhni Operatorin Aritmetik:")
print("1.Mbledhje")
print("2.Zbritje")
print("3.Shumzim")
print("4.Pjestim")

while True:
   
    choice = input("Zgjidhni:(1/2/3/4): ")

   
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Fusni Numrin e Pare: "))
        num2 = float(input("Fusni Numrin e Dyte: "))

        if choice == '1':
            print(num1, "+", num2, "=", mbledhje(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", zbritje(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", shumzim(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", pjestim(num1, num2))
            
            
        next_calculation = input("Deshironi te Vazhdoni ?  (po/jo): ")
        if next_calculation == "jo":

          break
    
    else:
        print("Invalid Input")  