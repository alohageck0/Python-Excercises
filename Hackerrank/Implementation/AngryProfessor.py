__author__ = 'royalfiish'

loops = int(input())
early = 0
for i in range(loops):
    cond = [int(x) for x in input().split(' ')]
    students = [int(x) for x in input().split(' ')]
    for _ in students:
        if _ <= 0:
            early += 1
    if early < cond[1]:
        print("YES")
    else:
        print("NO")
