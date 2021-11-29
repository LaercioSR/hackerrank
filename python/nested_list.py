if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    students_sorted = sorted(students, key=lambda d: (d[1], d[0]))
    
    set = []
    for x in students_sorted:
        if x[1] not in set:
            set.append(x[1])
    second_min = set[1]

    for x in filter(lambda x: x[1] == second_min, students_sorted):
        print(x[0])
