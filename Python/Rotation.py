side=[]
moving=0
file_name=""
def start():
    global side
    file = open(file_name, "r") 
    data = file.read()
    side = data.split("\n")
    side.pop()
    file.flush()
    
def stop():
    file = open(file_name, "w")
    for i in side:
        file.write(i+"\n")
    file.flush()

def rotate(s,end,dir):
    if s!=end and side[s][0]==side[s-moving][dir<0]:
        rotate(s-moving,end,dir)                  
    if dir==1:
        side[s]=side[s][1 : ] + side[s][0 : 1]
    else:
        side[s]=side[s][5 : ] + side[s][0 : 5]

def int2pattern(x):
    dic=['111','122','233','331','441','534','134','651','131','531']
    result=dic[int(x/10)] if x>9 else dic[0]
    result+=dic[x%10]
    return result

def step(x,m):
    pattern=int2pattern(x)
    global moving,file_name
    moving=m
    file_name="R_log.txt" if moving==1 else "L_log.txt"
    start()
    dir=1
    count=0
    steps=[]
    (s,end)=(5,0) if moving==1 else (0,5)
    for i in range(5,-1,-1) if moving==-1 else range(6):
        while pattern[i]!=side[i][0]:            
            rotate(s,end,dir)           
            count+=dir
        if count!=0: steps.append(round(count*84.9119341564))
        count=0
        dir*=-1
    stop()
    return steps

print(step(54, 1))