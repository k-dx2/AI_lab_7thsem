inp1 =[[3,1,4],[2,5,8], [7,0,6]]
inp = [[1,2,3],[0,4,5],[7,8,6]]
print("inp",inp,"->")
outp=[[1,2,3],[4,5,6],[7,8,0]]

def diff(inp,outp):
    count=0
    for i in range(0,3):
        for j in range(0,3):
            if inp[i][j] != outp[i][j]:
                count=count+1
    return count
    
def copylist(arr):
    operatedList=[]
    for i in range(0,3):
        localList=[]
        for j in range(0,3):
            localList.append(arr[i][j])
        operatedList.append(localList)
        
    return operatedList   
    
    
    
def steepestascent(inp):
    diffCount=diff(inp,outp)
    if diffCount == 0:
        print("SUCCESS")
        return
    
    list=[]
    for i in range(0,3):
        for j in range(0,3):
            if inp[i][j]==0:
                (x,y)=(i,j)
    
    #this is equivalent to left,right,up,down
    arry=[-1,0,0,1]
    arrx=[0,-1,1,0]
    
    
    for k in range(0,4):
        if x+arrx[k]>=0 and x+arrx[k]<3 and y+arry[k]>=0 and y+arry[k]<3 :
            operatedList=copylist(inp)
            operatedList[x][y]=operatedList[x+arrx[k]][y+arry[k]]
            operatedList[x+arrx[k]][y+arry[k]]=0
            list.append(operatedList)        
            
    
    for k in list:
        x = diff(k,outp)
        if x < diffCount:
            diffCount = x
            inp = k
	
    print(k,"->")
    steepestascent(inp)    

steepestascent(inp)

