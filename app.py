from calc_function import do_addition , do_subtraction ,do_multiplication ,do_divison
from expo import do_exponation
from area import find_area_rectangle

def main():
    print("Welcome to the Calculator APP")
    print("""\n Select the function
          1. Add
          2. Subtract
          3. Multiply
          4. Divide
          """)
    user_input = input("Select the Function :")

    a = int(input("Enter first number :"))
    b = int(input("Enter second number :"))

    if user_input == "1":
        result = do_addition(a,b)
    
    elif user_input == "2":
        result = do_subtraction(a,b)
    
    elif user_input == "3":
        result = do_multiplication(a,b)
    
    elif user_input == "4":
        result = do_divison(a,b)
    
    elif user_input == "5":
        result = do_exponation(a,b)
    
    elif user_input =="6":
        result = find_area_rectangle(a,b)

    print("Result",result)

if __name__ =="__main__":
    main()

