import os

spaceX = ["    "]
graphy = []
xValues = []
yValues = []

print("Welcome to the Native Python 3.8 Simple Parabola Grapher!")
a = input("Please enter your A value (Ax^2): ")
b = input("Please enter your B value (Bx): ")
c = input("Please enter your C value (C): ")
xLength = input("Please enter your desired x-axis length: ")

a = float(a)
b = float(b)
c = float(c)
xLength = int(xLength)

vertexX = ((-b)/(2*a))
maxY = ((a*vertexX*vertexX)+(b*vertexX)+c)
maxY2 = round(maxY)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

for i in range(0,int(maxY2)):
  if 9 >= int(maxY2)-i:
    graphy.append([str(int(maxY2-i))])
    graphy[i].append("  |")
  elif 10 <= int(maxY2)-i:
    graphy.append([str(int(maxY2-i))])
    graphy[i].append(" |")


def parabola(a, b, c):
  for i in range(0, int(xLength)+1):
    xValues.append(i)
    y = (a*i*i)+(b*i)+c
    if y >= 0:
      yValues.append(int(y))

def yScan(yValues, i):
  for k in range(0,i):
    if yValues[k] == yValues[i]:
      return True

def yScanGetIndex(yValues, i):
  return yValues.index(yValues[i])

def graph(xValues, yValues, graphy):
  cls()
  print("A="+str(a))
  print("B="+str(b))
  print("C="+str(c))
  print("\n")
  for i in range(0,len(yValues)):
    for j in range(0,len(graphy)):
      if yValues[i] == int(graphy[j][0]):
        if yScan(yValues, i) == True:
          k = yScanGetIndex(yValues, i)
          graphy[j].append((("   "*(xValues[i]-xValues[k])))[:-1]+"x")
        else:
          graphy[j].append("   "*xValues[i]+"x")
  for g in range(0,len(graphy)):
    print("".join(graphy[g]))    
  for j in range(0, int(xLength)+1):
    spaceX[0] = spaceX[0] + (str(j) + "  ")
  print(spaceX[0])

parabola(a,b,c)

graph(xValues, yValues, graphy)
