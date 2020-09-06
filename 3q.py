for i in range(int(input())):
  N=int(input())
  l=list(map(int,input().split()))
  m=[1]*N
  for j in range(0,len(l)-1):
   if(l[j]!=0):
     for k in range(j+1,len(l)):
         if(l[k]!=0 and l[k]!=l[j]):
              arr=(k-j)/(l[j]-l[k])
            #   print(arr)
              if(arr==int(arr) and arr>0):
                m[j]+=1
                m[k]+=1
  print(min(m),max(m),sep=" ")