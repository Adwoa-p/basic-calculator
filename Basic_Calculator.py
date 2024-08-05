while True:
    try:
        a=int(input("Enter First Number: "))
        b=int(input("Enter Second Number: "))
        operation=input("Input the kind of operation you want to perform(sum,product,difference or division): ")
        if operation== "sum":
            print(a+b)
        elif operation== "product":
            print(a*b)
        elif operation== "difference":
            print(a-b)
        elif operation== "division":
            print(a/b)
        
        prompt=input("Enter in to continue or out to exit: ")
        if prompt== "in":
            continue
        elif prompt== "out":
            break
    except ValueError as error:
        print(error)
    except ZeroDivisionError as error:
        print(error)
    except:
        print("An error Occured!!!")
    