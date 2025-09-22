
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("V�laszd ki a m�veletet")
print("1.�sszead�s")
print("2.Kivon�s")
print("3.Szorz�s")
print("4.Oszt�s")

while True:
    
    choice = input("V�lassz egy opci�t(1/2/3/4): ")

    
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Add meg az els� sz�mot: "))
            num2 = float(input("Add meg a m�sodik sz�mot: "))
        except ValueError:
            print("Hib�s k�d. Adj meg egy sz�mot.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        
        next_calculation = input("Csin�ljunk m�g egy sz�mol�st? (igen/nem): ")
        if next_calculation == "nem":
          break
    else:
        print("Hib�s k�d")
