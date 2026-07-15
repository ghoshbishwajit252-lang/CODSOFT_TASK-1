"""
SIMPLE CALCULATOR
Basic arithmetic operations: Addition, Subtraction, Multiplication, Division
"""

def display_menu():
    """Display the operation menu"""
    print("\n" + "="*40)
    print("         SIMPLE CALCULATOR")
    print("="*40)
    print("Choose an operation:")
    print("  1. Addition (+)")
    print("  2. Subtraction (-)")
    print("  3. Multiplication (*)")
    print("  4. Division (/)")
    print("  5. Exit")
    print("="*40)

def get_number(prompt):
    """Get a valid number from user input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

def get_operation():
    """Get a valid operation choice from user"""
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("❌ Please enter a number between 1 and 5.")
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

def perform_calculation(num1, num2, operation):
    """Perform the calculation based on operation choice"""
    if operation == 1:
        result = num1 + num2
        symbol = "+"
    elif operation == 2:
        result = num1 - num2
        symbol = "-"
    elif operation == 3:
        result = num1 * num2
        symbol = "×"
    elif operation == 4:
        if num2 == 0:
            return None, "❌ Error: Division by zero is not allowed!"
        result = num1 / num2
        symbol = "÷"
    else:
        return None, "Invalid operation"
    
    return result, f"{num1} {symbol} {num2} = {result}"

def main():
    """Main program loop"""
    print("\n🔢 Welcome to the Simple Calculator! 🔢")
    
    while True:
        display_menu()
        choice = get_operation()
        
        # Exit condition
        if choice == 5:
            print("\n👋 Thank you for using the calculator. Goodbye!")
            break
        
        # Get two numbers
        print("\n📝 Enter the two numbers:")
        num1 = get_number("  First number: ")
        num2 = get_number("  Second number: ")
        
        # Perform calculation
        result, message = perform_calculation(num1, num2, choice)
        
        # Display result
        print("\n" + "-"*40)
        if result is not None:
            print(f"✅ RESULT: {message}")
        else:
            print(f"❌ {message}")
        print("-"*40 + "\n")
        
        # Ask if user wants to continue
        while True:
            again = input("Do you want to perform another calculation? (y/n): ").lower()
            if again in ['y', 'yes']:
                break
            elif again in ['n', 'no']:
                print("\n👋 Thank you for using the calculator. Goodbye!")
                return
            else:
                print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()