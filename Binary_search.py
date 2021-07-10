def binary_srch(arr,l,r,x):
  if l<=r:
    mid=int((l+r)/2)
    if (arr[mid]==x):
      return mid
    elif arr[mid]>x:
      return binary_srch(arr,l,mid-1,x)
    else:
      return binary_srch(arr,mid+1,r,x)
  else:
    return -1
arr=[1,5,6,8,7,5]
key=8
binary_srch(arr,0,len(arr)-1,key)