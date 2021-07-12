def frkn(cost,weight,capacity):
  index=list(range(len(cost)))
  ratio=[c/w for c,w in zip(cost,weight)]
  index.sort(key=lambda i:ratio[i],reverse=True)
  profit=0
  for i in index:
    if (weight[i]<=capacity):
      profit+=cost[i]
      capacity-=weight[i]
    else:
      profit+=cost[i]*(capacity/weight[i])
      break
  return profit

cost=[100,60,120]
weight=[20,10,30]
capacity=50
profit=frkn(cost,weight,capacity)
print(profit)