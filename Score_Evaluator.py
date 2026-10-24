# Setting score thresholds
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

# Usage Implementation
print ("Welcome to the score evaluator!")
score = float(input("Please enter your score: "))
print("Your grade is:", evaluating_scores(score), "\nPlease come again!")
