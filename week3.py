#week 3
import numpy as np
ip=5
hiddn=[3,2,3]
op=1
network={}
for i in range(3):
  if i==0:
    weights=np.around(np.random.uniform(size=ip*hiddn[i]),decimals=3)
    bias=np.around(np.random.uniform(size=hiddn[i]),decimals=3)
  else:
    weights=np.around(np.random.uniform(size=hiddn[i]*hiddn[i-1]),decimals=3)
    bias=np.around(np.random.uniform(size=hiddn[i]),decimals=3)
  network[f"layer{i+1}"]={}
  network[f"layer{i+1}"]["weights"]=weights
  network[f"layer{i+1}"]["bias"]=bias
weights=np.around(np.random.uniform(size=hiddn[-1]*op),decimals=3)
bias=np.around(np.random.uniform(size=op),decimals=3)
network["layer4"]={}
network["layer4"]["weights"]=weights
network["layer4"]["bias"]=bias
print(network)
