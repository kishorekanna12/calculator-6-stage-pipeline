import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def menu():
    print("\n--- Menu-Driven Calculator (v1.0.0) ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Exit")
    
    choice = input("Enter choice (1-3): ")
    if choice == '3':
        sys.exit(0)
        
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        print(f"Result: {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {subtract(num1, num2)}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        while True:
            menu()