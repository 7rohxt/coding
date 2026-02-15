if __name__ == '__main__':
    records= []
    scores=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        i = [name,score]
        records.append(i)
        scores.append(i[1])
    
    # min_score = float('inf')
    # for j in scores:
    #     if j < min_score:
    #         min_score = j
    min_score = min(scores)
    
    second_min = min([k for k in scores if k > min_score])
    # second_min = float('inf')
    # for k in scores:
    #     if k > min_score and k<second_min:
    #         second_min = k
    
    second_lowest_students = sorted([n for n,s in records if s == second_min]) 
    
    for student in second_lowest_students:
        print(student)