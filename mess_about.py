# Write a program  to prompt for a score between 0.0 and 1.0
# If score is out of range, print an error message
# If score is within range, print grade 
# Score      Grade 
# >= 0.9        A
# >= 0.8        B
# >= 0.7        C
# >= 0.6        D
# < 0.6         F

inp = input('Enter score between 0.0 & 1.0: ')
score = float(inp)
score > 0.0 and score < 1.0

try:
    if score >= 0.9: 
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')    
    elif score >= 0.6:
        print('D')
    elif score < 0.6:
        print('F')
except:
    print('Bad Score! Please enter a valid number between 0.0 and 1.0')        