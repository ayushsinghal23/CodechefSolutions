# finding whether their is a valid sum or not
def betterfindingsum(b,N):
    half=sum(b)//2
    min_numbers_at_a_time=half//N +1
    for i in range(min_numbers_at_a_time,N-(min_numbers_at_a_time)):
        if(sum(b[0:i])==sum(b[i:N])):
            return 1
    return 0
# finding whether their is a valid sum or not
def findsum(b):
   i=-1
   j=len(b)
   sum_i=0
   sum_j=0
   while(i<j):
       i+=1
       sum_i += b[i]
       if(j!=i+1):
              j-=1
              sum_j+=b[j]
       while(sum_i<sum_j and i<j):
           i+=1
           sum_i+=b[i]
       while (sum_j < sum_i and i < j):
           j -= 1
           sum_j+= b[j]
       if(sum_i==sum_j and i==j-1):
          return 1
   return 0
for val in range(int(input())):
  N=int(input())
  l=list(range(1,N+1))
  print(l)
  print(sum(l))
  count=0
  if(sum(l)%2!=0):
    print("0")
  elif(sum(l)==6):
    print("2")
  else:
   for i in range(0,len(l)-1):
    for j in range(i+1,len(l)):
        b = l.copy()
        b[i],b[j]=b[j],b[i]
        count+=betterfindingsum(b,N)
        print(count)
        print(b)
   print(count)