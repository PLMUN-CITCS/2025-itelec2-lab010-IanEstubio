# IAN JAY P. ESTUBIO 
# Week 04 - Conditional Statements
# Laboratory # 10 - Guided Coding Exercise: if...elif...else Statement in Python

def main():
    """Main function to determine the letter grade based on numeric input."""
    
    try:
        user_input = input("Enter your numeric grade: ")
        grade = int(user_input)

        # Determine the letter grade
        if grade >= 90:
            letter_grade = "A"
        elif grade >= 80:
            letter_grade = "B"
        elif grade >= 70:
            letter_grade = "C"
        elif grade >= 60:
            letter_grade = "D"
        else:
            letter_grade = "F"
    
        print("Your grade is:", letter_grade)
    
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()


