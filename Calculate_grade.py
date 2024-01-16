# Calculate grades with your scores, and say whether you passed the course or not.

def calculate_grade(assignment_score, midterm_score, final_score):
    # How much each part is worth. Value can be changed. 
    weighted_grade = (assignment_score * 0.4) + (midterm_score * 0.3) + (final_score * 0.3)
    return weighted_grade

def get_valid_score(prompt):
    while True:
        try:
            score = float(input(f"Enter a score for {prompt}: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid, Enter a numeric value between 0 and 100.")
        except ValueError:
            print("Invalid, Enter a numeric value between 0 and 100.")

def display_result(grade):
    if grade >= 90:
        print(f"Grade: {grade:.2f}. Outstanding performance")
    elif grade >= 80:
        print(f"Grade: {grade:.2f}. Good work")
    elif grade >= 70:
        print(f"Grade: {grade:.2f}. Can improve")
    elif grade >= 60:
        print(f"Grade: {grade:.2f}. Passed")
    else:
        print(f"Grade: {grade:.2f}. Failed")

def main():
    while True:
        assignment_score = get_valid_score("Assignments")
        midterm_score = get_valid_score("Midterm")
        final_score = get_valid_score("Final")
        calculated_grade = calculate_grade(assignment_score, midterm_score, final_score)
        display_result(calculated_grade)
        

if __name__ == "__main":
    main()
