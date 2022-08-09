student_scores = input("Input a list of student scores ").split()
x = 0
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    # (if)when n = 0 there is no comparison 
    if n == 0:
        x = student_scores[n]  
    # (elif) but where there isn't if n -1 is greater than n -1 it becomes x
    elif student_scores[n] > x:
        x = student_scores[n]
    # (else) n is x 
print(x)