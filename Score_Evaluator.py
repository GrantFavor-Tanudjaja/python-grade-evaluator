# Function defining score thresholds
def evaluating_scores(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score >= 50:
        return "pass"
    else:
        return "fail"

# Main Interactive Program Loop
print ("----Welcome to the score evaluator!----")
intention = input("\nWould you like to evaluate your score? (yes/no): ").strip().lower()

if intention == "yes":
    while True:
        user_input = input("\nPlease enter your score (0-100) or type 'q' to quit: ").strip().lower()
        if user_input == 'q':
            print("\n----Thank you for using the score evaluator. See you next time!----")
            break
        try:
            score = float(user_input)
            if 0 <= score <= 100:
                print(f"\nYour grade is: {evaluating_scores(score)}")
            else:
                print("\nError : Score must be between 0 and 100. Please try again.")
        except ValueError:
            print("\nError : Invalid input. Please enter a valid numerical score between 0 and 100 or press 'q' to quit.")
else:
    print("\n----Thank you for using the score evaluator. See you next time!----")
    