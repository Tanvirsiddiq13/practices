def arrange_data(student_number):
    scores = {}
    
    for _ in range(student_number):
        student_id = input("student id:")
        score = int(input("score:"))
        scores[student_id] = score
    
    sorted_scores = sorted(scores.items())

    for student, score in sorted_scores:

        print(f"Student ID: {student}, Score: {score}")
        if score > 59:
            print(f"student id {student} is pass")
        else:
            print(f"student id {student} is fail")

if __name__ == "__main__":
    student_number = int(input("student number:"))
    arrange_data(student_number)

