

def fact(x):
    if x==0 or x==1:
        return 1
    return fact(x-1)*x 
        


what=input("Add any number:")


if what.isdigit():

    number=int(what)
    result=fact(number)

    print(f"The factorial of {number} is {result}.")


elif what.lower() == "x":
        print("хуй.")


else:
    print("Хуйню не неси")



        

    
