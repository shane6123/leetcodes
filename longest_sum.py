arr = [-2, -3, 4, 1, -2, 1, 5, -3]
s = 0
l=0
for i in range(len(arr)):
    for j in range(i, len(arr)):
        print(arr[i:j + 1])
        # s=max(s,sum(arr[i:j+1]))
        new=sum(arr[i:j+1])
        if s<new:
            s=new
            l=len(arr[i:j+1])

        
print(s,l)
