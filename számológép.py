
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Válaszd ki a mûveletet")
print("1.Összeadás")
print("2.Kivonás")
print("3.Szorzás")
print("4.Osztás")

while True:
    
    choice = input("Válassz egy opciót(1/2/3/4): ")

    
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Add meg az elsõ számot: "))
            num2 = float(input("Add meg a második számot: "))
        except ValueError:
            print("Hibás kód. Adj meg egy számot.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        
        next_calculation = input("Csináljunk még egy számolást? (igen/nem): ")
        if next_calculation == "nem":
          break
    else:
        print("Hibás kód")
