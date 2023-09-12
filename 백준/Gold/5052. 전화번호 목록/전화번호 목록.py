for i in range(int(input())):
    a=0
    db=[]
    for j in range(int(input())):
        db.append(input())
    db.sort()
    for j in range(len(db)-1):
        if db[j][:min(len(db[j]),len(db[j+1]))]==db[j+1][:min(len(db[j]),len(db[j+1]))]:
            print("NO")
            a+=1
            break
    if a!=1:
        print("YES")