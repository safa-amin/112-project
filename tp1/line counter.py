import os
# assign directory
directory = 'tp1'
fileList = []
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        f = f[6:]
        if f != "line counter.py":
          fileList.append(f)
            
            

L = []
total = 0
for file in fileList:
  count = 0
  f = open(f"files/{file}", "r")
  for l in f:
    l = l.strip()
    if l and not l.startswith('#'):
        count += 1
  total +=count
  L.append((file,count))
print(L)
print("total is", total)