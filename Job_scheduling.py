def jobs(arr,t):
  n=len(arr)
  for i  in range(n):
    for j in range(n-1-i):
      if(arr[j][2]<arr[j+1][2]):
        arr[j],arr[j+1]=arr[j+1],arr[j]
  result=[False]*t
  job=['0']*t
  for i in range(n):
    for j in range((arr[i][1]-1),-1,-1):
      if (result[j] is False):
        result[j]=True
        job[j]=arr[i][0]
        break
  print(job)

arr=[['a',2,100],['d',2,500],['e',3,10]]
jobs(arr,3)