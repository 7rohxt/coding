if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    total = 0
    for name,marks in student_marks.items():
        if name==query_name:
            for i in marks:
                total += i
    

    print(f"{total/3:.2f}") 
    
    # if query_name in student_marks:
    # avg_score = sum(student_marks[query_name]) / 3 
    # print(f"{avg_score:.2f}") 