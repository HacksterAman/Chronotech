side=[]
def start():
    global side
    file = open("log.txt", "r")
    data = file.read()
    side = data.split("\n")
    side.pop()
    file.close()
    
def stop():
    file = open("log.txt", "w")
    for i in side:
        file.write(i+"\n")
    file.close()

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
 
def step(pattern):
    start()
    dir=1
    count=0
    steps=[]
    for i in range(5,-1,-1):
        while pattern[i]!=side[i][0]:
            if dir:
                leftrotate()
                count+=1
            else:
                rightrotate()
                count-=1
        dir=not dir
        steps.append(count)
        count=0
    stop()
    return steps

print(step('123456'))