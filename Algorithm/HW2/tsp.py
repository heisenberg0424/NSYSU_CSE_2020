import sys
import math
import numpy as np
import copy
import time
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TKAgg')
#FUNC
def distance(a,b):
    ans=math.sqrt((input[a][1]-input[b][1])**2+(input[a][2]-input[b][2])**2)
    return ans

def TSP(done,ndone):
    if(done,ndone) in cal:
        return cal[done,ndone]
    
    nextstep_status=[]
    nextstep_values=[]

    for i in ndone:
        nextstep=copy.deepcopy(list(ndone))
        nextstep.remove(i)
        nextstep_status.append([i,tuple(nextstep)])
        dis=TSP(i,tuple(nextstep))
        nextstep_values.append(dis+data[done-1][i-1])
    
    cal[done,ndone]=min(nextstep_values)
    track.append(((done,ndone),nextstep_status[nextstep_values.index(min(nextstep_values))]))
    return cal[done,ndone]

#Main
start=time.time()
file=open(sys.argv[1],'r')
input=[]
track=[]
cal={}
undo=[]
graph=[]
#read file
for line in file:
    name,x,y=line.split(' ')
    input.append([int(name),int(x),int(y)])
stations=len(input)
data=np.zeros((stations,stations))
#calculate distance between each stations
for i in range(stations):
    for j in range(stations):
        data[i][j]=distance(i,j)
#initialize dp's graph
for x in range(1,stations):
    cal[x+1,()]=data[x][0]

for i in range(1,stations):
    undo.append(i+1)
undo=tuple(undo)
TSP(1,undo)
temp=track.pop()
end=time.time()
output=open('output.txt','w+')
print('Best visit order: ',input[0][0],sep='',end=" , ")
output.write('Best visit order: %d , ' %input[0][0])
graph.append(input[0])
print(input[temp[1][0]-1][0],end=' , ')
output.write('%d , ' %(input[temp[1][0]-1][0]))
graph.append(input[temp[1][0]-1])
for _ in range(stations-2):
    for i in track:
        if tuple(temp[1])==i[0]:
            print(input[i[1][0]-1][0],end=' , ')
            output.write('%d , ' %(input[i[1][0]-1][0]))
            graph.append(input[i[1][0]-1])
            temp=i
print(input[0][0])
output.write('%d\n' %input[0][0])
graph.append(input[0])
print('Best Distance: ',cal[(1,undo)],sep='')
temp=cal[(1,undo)]
output.write('Best Distance: %f\n' %(temp))
print('Execution Time: ',end-start,sep='')
output.write('Execution Time: %f\n' %(end-start))
output.close()
file.close()

#Graph
x=[]
y=[]
for i in graph:
    x.append(i[1])
    y.append(i[2])
plt.plot(x,y,'r-')
plt.savefig('output.png')
