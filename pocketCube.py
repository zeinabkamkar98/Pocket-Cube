import copy
##########################################################
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

queue=Queue()

##########################################################
def bfs(state):
    
    queue.enqueue(state)
    
    while True:
        
        current_state=queue.dequeue()
        
        child1=one(copy.deepcopy(current_state))
        if(child1['is_goal']==24):
            return child1
        else:
            queue.enqueue(child1)
    
        child2=two(copy.deepcopy(current_state))
        if(child2['is_goal']==24):
            return child2
        else:
            queue.enqueue(child2)
    
        child3=three(copy.deepcopy(current_state))
        if(child3['is_goal']==24):
            return child3
        else:
            queue.enqueue(child3)
    
        child4=four(copy.deepcopy(current_state))
        if(child4['is_goal']==24):
            return child4
        else:
            queue.enqueue(child4)
    
        child5=five(copy.deepcopy(current_state))
        if(child5['is_goal']==24):
            return child5
        else:
            queue.enqueue(child5)
    
        child6=six(copy.deepcopy(current_state))
        if(child6['is_goal']==24):
            return child6
        else:
            queue.enqueue(child6)
    
        child7=seven(copy.deepcopy(current_state))
        if(child7['is_goal']==24):
            return child7
        else:
            queue.enqueue(child7)
    
        child8=eight(copy.deepcopy(current_state))
        if(child8['is_goal']==24):
            return child8
        else:
            queue.enqueue(child8)
    
        child9=nine(copy.deepcopy(current_state))
        if(child9['is_goal']==24):
            return child9
        else:
            queue.enqueue(child9)
    
        child10=ten(copy.deepcopy(current_state))
        if(child10['is_goal']==24):
            return child10
        else:
            queue.enqueue(child10)
    
        child11=eleven(copy.deepcopy(current_state))
        if(child11['is_goal']==24):
            return child11
        else:
            queue.enqueue(child11)
    
        child12=twelve(copy.deepcopy(current_state))
        if(child12['is_goal']==24):
            return child12
        else:
            queue.enqueue(child12)
    
    return state
        
#############################################################
def is_goal(state):
    
    count=0
    
    if state['l1']=='w':
        count=count+1
    if state['l2']=='w':
        count=count+1
    if state['l3']=='w':
        count=count+1
    if state['l4']=='w':
        count=count+1
        
    if state['u1']=='b':
        count=count+1
    if state['u2']=='b':
        count=count+1
    if state['u3']=='b':
        count=count+1
    if state['u4']=='b':
        count=count+1
        
    if state['f1']=='r':
        count=count+1
    if state['f2']=='r':
        count=count+1
    if state['f3']=='r':
        count=count+1
    if state['f4']=='r':
        count=count+1
        
    if state['d1']=='g':
        count=count+1
    if state['d2']=='g':
        count=count+1
    if state['d3']=='g':
        count=count+1
    if state['d4']=='g':
        count=count+1

    if state['r1']=='y':
        count=count+1
    if state['r2']=='y':
        count=count+1
    if state['r3']=='y':
        count=count+1
    if state['r4']=='y':
        count=count+1

    if state['b1']=='o':
        count=count+1
    if state['b2']=='o':
        count=count+1
    if state['b3']=='o':
        count=count+1
    if state['b4']=='o':
        count=count+1

    return count

#############################################################
#moves
def one(state):
    #actions
    
    temp0=state['l1']
    state['l1']=state['l2']
    state['l2']=state['l4']
    state['l4']=state['l3']
    state['l3']=temp0
    
    
    temp1=state['u1']
    temp2=state['u3']
    
    state['u1']=state['f1']
    state['u3']=state['f3']

    state['f1']=state['d1']
    state['f3']=state['d3']

    state['d1']=state['b4']
    state['d3']=state['b2']

    state['b4']=temp1
    state['b2']=temp2    
    
    
    
    state['is_goal']=is_goal(state)
    state['path'].append(1)
    return state

def two(state):
    #actions

    temp0=state['l1']
    state['l1']=state['l3']
    state['l3']=state['l4']
    state['l4']=state['l2']
    state['l2']=temp0
    
    
    temp1=state['u1']
    temp2=state['u3']
    
    state['u1']=state['b4']
    state['u3']=state['b2']

    state['b2']=state['d3']
    state['b4']=state['d1']

    state['d1']=state['f1']
    state['d3']=state['f3']

    state['f1']=temp1
    state['f3']=temp2    
    

    state['is_goal']=is_goal(state)
    state['path'].append(2)
    return state
def three(state):
    #actions
    
    temp0=state['r1']
    state['r1']=state['r3']
    state['r3']=state['r4']
    state['r4']=state['r2']
    state['r2']=temp0
    
    
    temp1=state['u2']
    temp2=state['u4']
    
    state['u2']=state['f2']
    state['u4']=state['f4']

    state['f2']=state['d2']
    state['f4']=state['d4']

    state['d2']=state['b3']
    state['d4']=state['b1']

    state['b3']=temp1
    state['b1']=temp2    
    

    state['is_goal']=is_goal(state)
    state['path'].append(3)
    return state

def four(state):
    #actions
    
    temp0=state['r1']
    state['r1']=state['r2']
    state['r2']=state['r4']
    state['r4']=state['r3']
    state['r3']=temp0
      
    
    temp1=state['u2']
    temp2=state['u4']
    
    state['u2']=state['b3']
    state['u4']=state['b1']

    state['b3']=state['d2']
    state['b1']=state['d4']

    state['d2']=state['f2']
    state['d4']=state['f4']

    state['f2']=temp1
    state['f4']=temp2    
    
    
    state['is_goal']=is_goal(state)
    state['path'].append(4)
    return state

def five(state):
    #actions
    
    temp0=state['f1']
    state['f1']=state['f2']
    state['f2']=state['f4']
    state['f4']=state['f3']
    state['f3']=temp0
    
    
    temp1=state['u3']
    temp2=state['u4']
    
    state['u3']=state['r1']
    state['u4']=state['r3']

    state['r1']=state['d2']
    state['r3']=state['d1']

    state['d1']=state['l2']
    state['d2']=state['l4']

    state['l2']=temp2
    state['l4']=temp1    
    

    state['is_goal']=is_goal(state)
    state['path'].append(5)
    return state

def six(state):
    #actions
    
    temp0=state['f1']
    state['f1']=state['f3']
    state['f3']=state['f4']
    state['f4']=state['f2']
    state['f2']=temp0
       
    
    temp1=state['u3']
    temp2=state['u4']
    
    state['u3']=state['l4']
    state['u4']=state['l2']

    state['l2']=state['d1']
    state['l4']=state['d2']

    state['d1']=state['r3']
    state['d2']=state['r1']

    state['r1']=temp1
    state['r3']=temp2    
    

    state['is_goal']=is_goal(state)
    state['path'].append(6)
    return state

def seven(state):
    #actions
    
    temp0=state['b1']
    state['b1']=state['b3']
    state['b3']=state['b4']
    state['b4']=state['b2']
    state['b2']=temp0
    
    
    temp1=state['u1']
    temp2=state['u2']
    
    state['u1']=state['r2']
    state['u2']=state['r4']

    state['r2']=state['d4']
    state['r4']=state['d3']

    state['d3']=state['l1']
    state['d4']=state['l3']

    state['l3']=temp1
    state['l1']=temp2    
    


    state['is_goal']=is_goal(state)
    state['path'].append(7)
    return state

def eight(state):
    #actions
    
    temp0=state['b1']
    state['b1']=state['b2']
    state['b2']=state['b4']
    state['b4']=state['b3']
    state['b3']=temp0
    
    temp1=state['u1']
    temp2=state['u2']
    
    state['u1']=state['l3']
    state['u2']=state['l1']

    state['l1']=state['d3']
    state['l3']=state['d4']

    state['d3']=state['r4']
    state['d4']=state['r2']

    state['r2']=temp1
    state['r4']=temp2    
   

    state['is_goal']=is_goal(state)
    state['path'].append(8)
    return state

def nine(state):
    #actions
    
    temp0=state['u1']
    state['u1']=state['u2']
    state['u2']=state['u4']
    state['u4']=state['u3']
    state['u3']=temp0
   

    temp1=state['l1']
    temp2=state['l2']
    
    state['l1']=state['b1']
    state['l2']=state['b2']

    state['b1']=state['r1']
    state['b2']=state['r2']

    state['r1']=state['f1']
    state['r2']=state['f2']

    state['f1']=temp1
    state['f2']=temp2    
    

    state['is_goal']=is_goal(state)
    state['path'].append(9)
    return state

def ten(state):
    #actions
    
    temp0=state['u1']
    state['u1']=state['u3']
    state['u3']=state['u4']
    state['u4']=state['u2']
    state['u2']=temp0
  
    
    temp1=state['l1']
    temp2=state['l2']
    
    state['l1']=state['f1']
    state['l2']=state['f2']

    state['f1']=state['r1']
    state['f2']=state['r2']

    state['r1']=state['b1']
    state['r2']=state['b2']

    state['b1']=temp1
    state['b2']=temp2    
   

    state['is_goal']=is_goal(state)
    state['path'].append(10)
    return state

def eleven(state):
    #actions
    
    temp0=state['d1']
    state['d1']=state['d3']
    state['d3']=state['d4']
    state['d4']=state['d2']
    state['d2']=temp0
   
    
    temp1=state['l3']
    temp2=state['l4']
    
    state['l3']=state['b3']
    state['l4']=state['b4']

    state['b3']=state['r3']
    state['b4']=state['r4']

    state['r3']=state['f3']
    state['r4']=state['f4']

    state['f3']=temp1
    state['f4']=temp2    
   
    state['is_goal']=is_goal(state)
    state['path'].append(11)
    return state

def twelve(state):
    #actions
    
    temp0=state['d1']
    state['d1']=state['d2']
    state['d2']=state['d4']
    state['d4']=state['d3']
    state['d3']=temp0
    
    temp1=state['l3']
    temp2=state['l4']
    
    state['l3']=state['f3']
    state['l4']=state['f4']

    state['f3']=state['r3']
    state['f4']=state['r4']

    state['r3']=state['b3']
    state['r4']=state['b4']

    state['b3']=temp1
    state['b4']=temp2    
  

    state['is_goal']=is_goal(state)
    state['path'].append(12)
    return state

#############################################################
#read file
from sys import stdin
file = stdin
#file=open("input.txt")
data=file.readlines()
#############################################################
init_state={'path':[]}

for d in range(len(data)):
    
    if d==0:
        color=data[d].split()
        init_state['l1']=color[0]
        init_state['l2']=color[1]
        init_state['l3']=color[2]
        init_state['l4']=color[3]

    elif d==1:
        color=data[d].split()
        init_state['u1']=color[0]
        init_state['u2']=color[1]
        init_state['u3']=color[2]
        init_state['u4']=color[3]

    elif d==2:
        color=data[d].split()
        init_state['f1']=color[0]
        init_state['f2']=color[1]
        init_state['f3']=color[2]
        init_state['f4']=color[3]

    elif d==3:
        color=data[d].split()
        init_state['d1']=color[0]
        init_state['d2']=color[1]
        init_state['d3']=color[2]
        init_state['d4']=color[3]

    elif d==4:
        color=data[d].split()
        init_state['r1']=color[0]
        init_state['r2']=color[1]
        init_state['r3']=color[2]
        init_state['r4']=color[3]

    else:
        color=data[d].split()
        init_state['b1']=color[0]
        init_state['b2']=color[1]
        init_state['b3']=color[2]
        init_state['b4']=color[3]

    
    
a=bfs(copy.deepcopy(init_state))
for i in a['path']:
    print(i, end = ' ')  
    
    
    
    
    
    
    
    