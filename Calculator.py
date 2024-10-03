def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def calculator():
    print("Welcome to the Simple Calculator!")
    
    while True:
        try:
            # Input numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            # Choose operation
            print("\nChoose an operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            
            choice = input("Enter your choice (1/2/3/4): ")
            
            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"
            else:
                print("Invalid choice! Please select a valid operation.")
                continue
            
            # Print the result
            print(f"\n{num1} {operation} {num2} = {result}\n")
            
            # Option to continue or exit
            again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if again != 'yes':
                print("Thank you for using the calculator. Goodbye!")
                break
                
        except ValueError:
            print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    calculator()
