def mergesrt(lst):
  if (len(lst)>1):
    mid=int(len(lst)/2)
    left=lst[:mid]
    right=lst[mid:]
    mergesrt(left)
    mergesrt(right)
    i=j=k=0
    while (i<len(left) and j<len(right)):
      if(left[i]<right[j]):
       lst[k]=left[i]
       i=i+1
       k=k+1
      else:
        lst[k]=right[j]
        j=j+1
        k=k+1
    while (i<len(left)):
      lst[k]=left[i]
      i=i+1
      k=k+1
    while (j<len(right)):
      lst[k]=right[j]
      j=j+1
      k=k+1
  return lst
lst=[5,7,8,4,2,1,5,0,54,87,985]
mergesrt(lst)
      