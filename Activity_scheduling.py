def actsel(s,f):
  index=[i for i in range(len(s))]
  index.sort(key=lambda i:f[i])
  activity=[]
  activity+=[index[0]]
  f_time=f[index[0]]
  for k in range(1,len(index)):
    ind=index[k]
    if (s[ind]>=f_time):
      activity+=[ind]
      f_time=f[ind]
  return activity

s=[1,4,5,6,7]
f=[2,3,1,4,5]
activity=actsel(s,f)
print(activity)