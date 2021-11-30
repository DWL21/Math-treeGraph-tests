import treeGraph as tg

dicMatrix = {}
dicAnswer = {}
dicResult = {}
answerCases = []
wrongCases = []

def printResultAnswer(name, result, answer):
    print("-"*100)
    print(f"{name} result: {result}")
    dicResult[name] = result
    dicAnswer[name] = answer
    if (result == answer):
        print(f"{name}: Success")
        answerCases.append(name)
    else:
        print(f"{name}: Failure")
        wrongCases.append(name)

def printResult(answerCases, wrongCases):
    allCases = answerCases + wrongCases
    answerCases.sort()
    wrongCases.sort()
    allCases.sort()
    lenAnswer = len(answerCases)
    lennoAnswer = len(wrongCases)
    lenAll = len(allCases)
    print("-"*100)
    print(f"All: {allCases}")
    print(f"Success: {answerCases}")
    print(f"Failure: {wrongCases}")
    print()
    print(f"(Success/All): ({lenAnswer}/{lenAll})")
    if(lenAll == lenAnswer):
        print("Passed all tests.")
    else:
        print(f"Passed {lenAnswer} tests.")

def makeMatrix(myVertex, myInfo):
    lenVertex = len(myVertex)
    myMatrix = [[0]*lenVertex for _ in range(lenVertex)]
    for i in range(lenVertex):
        myMatrix[i][i] = tg.INF
    for i in range(lenVertex-1):
        k = 0
        for j in range(lenVertex-1):
            if(k == len(myInfo[i])):
                break
            myMatrix[i][-(j+1)] = myInfo[i][-(j+1)]
            myMatrix[-(j+1)][i] = myInfo[i][-(j+1)]
            k += 1
    return myMatrix


print("testTree.py")

lenVertex = 4
myInfo = [[3, 2, 5], [4, 2], [7]]
myVertex = [i+1 for i in range(lenVertex)]
myMatrix = makeMatrix(myVertex, myInfo)
print(myMatrix)
graphAnswer = 7
a = tg.myGraph(myVertex, myMatrix)
name = "a"
self = a
graphResult = self.MST()
dicMatrix[name] = myMatrix
printResultAnswer(name, graphResult, graphAnswer)

lenVertex = 4
myInfo = [[5, 3, tg.INF], [2, 3], [tg.INF]]
myVertex = [i+1 for i in range(lenVertex)]
myMatrix = makeMatrix(myVertex, myInfo)
print(myMatrix)
graphAnswer = 8
b = tg.myGraph(myVertex, myMatrix)
name = "b"
self = b
graphResult = self.MST()
dicMatrix[name] = myMatrix
printResultAnswer(name, graphResult, graphAnswer)

lenVertex = 3
myInfo = [[3, 3], [tg.INF]]
myVertex = [i+1 for i in range(lenVertex)]
myMatrix = makeMatrix(myVertex, myInfo)
print(myMatrix)
graphAnswer = 6
c = tg.myGraph(myVertex, myMatrix)
name = "c"
self = c
graphResult = self.MST()
dicMatrix[name] = myMatrix
printResultAnswer(name, graphResult, graphAnswer)

lenVertex = 2
myInfo = [[3]]
myVertex = [i+1 for i in range(lenVertex)]
myMatrix = makeMatrix(myVertex, myInfo)
print(myMatrix)
graphAnswer = 3
d = tg.myGraph(myVertex, myMatrix)
name = "d"
self = d
graphResult = self.MST()
dicMatrix[name] = myMatrix
printResultAnswer(name, graphResult, graphAnswer)

lenVertex = 1
myInfo = []
myVertex = [i+1 for i in range(lenVertex)]
myMatrix = makeMatrix(myVertex, myInfo)
print(myMatrix)
graphAnswer = 0
e = tg.myGraph(myVertex, myMatrix)
name = "e"
self = e
graphResult = self.MST()
dicMatrix[name] = myMatrix
printResultAnswer(name, graphResult, graphAnswer)

lenVertex = 3
myInfo = [[2, 5], [tg.INF]]
myVertex = [i+1 for i in range(lenVertex)]
myMatrix = makeMatrix(myVertex, myInfo)
print(myMatrix)
graphAnswer = 7
f = tg.myGraph(myVertex, myMatrix)
name = "f"
self = f
graphResult = self.MST()
dicMatrix[name] = myMatrix
printResultAnswer(name, graphResult, graphAnswer)

printResult(answerCases, wrongCases)

lenVertex = 6
myInfo = [[2, 5, 4, 6, 7], [4, 5, 6, 10], [20, 3, 4], [2, 30], [tg.INF]]
myVertex = [i+1 for i in range(lenVertex)]
myMatrix = makeMatrix(myVertex, myInfo)
print(myMatrix)
graphAnswer = 17
g = tg.myGraph(myVertex, myMatrix)
name = "g"
self = g
graphResult = self.MST()
dicMatrix[name] = myMatrix
printResultAnswer(name, graphResult, graphAnswer)

lenVertex = 5
myInfo = [[4, 5, 10, 20], [3, tg.INF, 7], [1, 2], [5]]
myVertex = [i+1 for i in range(lenVertex)]
myMatrix = makeMatrix(myVertex, myInfo)
print(myMatrix)
graphAnswer = 10
h = tg.myGraph(myVertex, myMatrix)
name = "h"
self = h
graphResult = self.MST()
dicMatrix[name] = myMatrix
printResultAnswer(name, graphResult, graphAnswer)

lenVertex = 5
myInfo = [[2, 2, 2, 2], [2, 2, 2], [2, 2], [2]]
myVertex = [i+1 for i in range(lenVertex)]
myMatrix = makeMatrix(myVertex, myInfo)
print(myMatrix)
graphAnswer = 8
i = tg.myGraph(myVertex, myMatrix)
name = "i"
self = i
graphResult = self.MST()
dicMatrix[name] = myMatrix
printResultAnswer(name, graphResult, graphAnswer)

lenVertex = 7
myInfo = [[2, 1, 5, 2, tg.INF, 3], [3, 5, tg.INF, 1, 8], [4, 3, 2, 6], [3, 2, 8], [3, 5], [2]]
myVertex = [i+1 for i in range(lenVertex)]
myMatrix = makeMatrix(myVertex, myInfo)
print(myMatrix)
graphAnswer = 11
j = tg.myGraph(myVertex, myMatrix)
name = "j"
self = j
graphResult = self.MST()
dicMatrix[name] = myMatrix
printResultAnswer(name, graphResult, graphAnswer)

printResult(answerCases, wrongCases)


while(1):
    print("-"*100)
    name = input("Please enter the name (Exit: 0): ")
    if name == '0':
        print("Exit")
        break
    print("-"*100)
    for i in range(len(dicMatrix[name])):
        print(dicMatrix[name][i])
    print("-"*100)
    print(f"Vertex: {len(dicMatrix[name])}")
    print(f"Result: {dicResult[name]}")
    print(f"Answer : {dicAnswer[name]}")