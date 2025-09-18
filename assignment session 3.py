def make_student(name, scores):
    total_score = sum(scores)
    average = total_score / len(scores)
    return {
        "name" : name,
        "scores" : scores,
        "average" : average
    }

def classroom(students):
    top_student = None
    highest_average_score = 0

    for student in students:
        if student["average"] > highest_average_score:
            highest_average_score = student["average"]
            top_student = student["name"]
        
    return top_student

# Main program
student1 = make_student("Asep", [80, 85, 95])
student2 = make_student("Budi", [90, 95, 100])
student3 = make_student("Agus", [85, 80, 80])

students = [student1, student2, student3]

print("The top student in the class is:", classroom(students))