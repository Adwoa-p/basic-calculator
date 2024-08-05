while True:
    a=int(input("Enter a value: "))
    b=int(input("Enter a value: "))
    operation=input("Input the kind of operation you want to perform(sum,product,difference or division): ")
    if operation== "sum":
        print(a+b)
    elif operation== "product":
        print(a*b)
    elif operation== "difference":
        print(a-b)
    elif operation== "division":
        if b!=0:
               print(a/b)
        else:
            print("Math Error")
    prompt=input("Enter in to continue or out to exit: ")
    if prompt== "in":
        continue
    elif prompt== "out":
        break
    