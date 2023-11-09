side=[[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]
dir=1
count=0
steps=[]

def leftrotate(s=0):
    if s!=5:
        if side[s][0]==side[s+1][0]:
            leftrotate(s+1)
    side[s]=side[s][1 : ] + side[s][0 : 1]
   
def rightrotate(s=0):
    if s!=5:
        if side[s][0]==side[s+1][1]:
            rightrotate(s+1)
    side[s]=side[s][5 : ] + side[s][0 : 5]

def rotate():
    global dir, count
    if dir:
        leftrotate()
        count+=1
    else:
        rightrotate()
        count-=1
    
pattern=input("Enter the pattern:\n")
for i in range(5,-1,-1):
    while int(pattern[i])!=side[i][0]:
        rotate()
    dir=not dir
    steps.append(count)
    print(count)
    count=0
    for i in range(0,6):
        print(side[i])
    print('-------------------')
print("Steps required: ",steps)