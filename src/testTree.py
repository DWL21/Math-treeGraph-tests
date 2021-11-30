import treeGraph as tg

answerCases = []
wrongCases = []

def printResultAnswer(name, treeResult, treeAnswer):
    print("-"*100)
    print(f"{name} result: {treeResult}")
    if (treeResult == treeAnswer):
        print(f"{name}: 정답")
        answerCases.append(name)
    else:
        print(f"{name} answer: {treeAnswer}")
        print(f"{name}: 오답")
        wrongCases.append(name)


def printResult(answerCases, wrongCases):
    allCases = answerCases + wrongCases
    answerCases.sort()
    wrongCases.sort()
    allCases.sort()
    allCases
    lenAnswer = len(answerCases)
    lennoAnswer = len(wrongCases)
    lenAll = len(allCases)
    print("-"*100)
    print(f"전체: {allCases}")
    print(f"통과: {answerCases}")
    print(f"실패: {wrongCases}")
    print()
    print(f"(성공/전체): ({lenAnswer}/{lenAll})")
    if(lenAll == lenAnswer):
        print("모든 테스트를 통과 하였습니다.")
    else:
        print(f"{lenAnswer}개의 테스트를 통과 하였습니다.")


print("testTree.py")

t = tg.myTree()
self = t
name = "t"
self.addInfo('A', ['B', 'C'])
self.addInfo('B', ['D', '.'])
self.addInfo('C', ['E', 'F'])
self.addInfo('D', ['.', '.'])
self.addInfo('E', ['.', '.'])
self.addInfo('F', ['.', 'G'])
self.addInfo('G', ['.', '.'])
treeResult = self.postorder('A')
treeAnswer = ['D', 'B', 'E', 'G', 'F', 'C', 'A']
printResultAnswer(name, treeResult, treeAnswer)

a = tg.myTree()
self = a
name = "a"
self.addInfo('A', ['B', 'C'])
self.addInfo('B', ['D', 'F'])
self.addInfo('C', ['J', 'K'])
self.addInfo('D', ['G', 'H'])
self.addInfo('E', ['.', '.'])
self.addInfo('F', ['I', '.'])
self.addInfo('G', ['E', '.'])
self.addInfo('H', ['.', '.'])
self.addInfo('I', ['O', 'P'])
self.addInfo('J', ['L', 'M'])
self.addInfo('K', ['N', '.'])
self.addInfo('L', ['.', '.'])
self.addInfo('M', ['Q', 'R'])
self.addInfo('N', ['.', '.'])
self.addInfo('O', ['.', '.'])
self.addInfo('P', ['.', '.'])
self.addInfo('Q', ['.', '.'])
self.addInfo('R', ['S', '.'])
self.addInfo('S', ['.', '.'])
treeAnswer = ['E', 'G', 'H', 'D', 'O', 'P', 'I', 'F', 'B', 'L', 'Q',\
     'S', 'R', 'M', 'J', 'N', 'K', 'C', 'A']
treeResult = self.postorder('A')
printResultAnswer(name, treeResult, treeAnswer)

b = tg.myTree()
name = "b"
self = b
self.addInfo('A', ['B', '.'])
self.addInfo('B', ['C', '.'])
self.addInfo('C', ['D', 'E'])
self.addInfo('D', ['I', '.'])
self.addInfo('E', ['F', '.'])
self.addInfo('F', ['G', 'H'])
self.addInfo('G', ['.', '.'])
self.addInfo('H', ['.', '.'])
self.addInfo('I', ['J', 'K'])
self.addInfo('J', ['.', '.'])
self.addInfo('K', ['.', '.'])
treeResult = self.postorder('A')
treeAnswer = ['J', 'K', 'I', 'D', 'G', 'H', 'F', 'E', 'C', 'B', 'A']
printResultAnswer(name, treeResult, treeAnswer)

c = tg.myTree()
name = "c"
self = c
self.addInfo('A', ['.', '.'])
treeResult = self.postorder('A')
treeAnswer = ['A']
printResultAnswer(name, treeResult, treeAnswer)

d = tg.myTree()
name = "d"
self = d
self.addInfo('A', ['B', 'C'])
self.addInfo('B', ['D', 'F'])
self.addInfo('C', ['G', 'I'])
self.addInfo('D', ['.', '.'])
self.addInfo('F', ['H', '.'])
self.addInfo('G', ['.', '.'])
self.addInfo('H', ['.', '.'])
self.addInfo('I', ['.', '.'])
treeResult = self.postorder('A')
treeAnswer = ['D', 'H', 'F', 'B', 'G', 'I', 'C', 'A']
printResultAnswer(name, treeResult, treeAnswer)

e = tg.myTree()
name = "e"
self = e
self.addInfo('A', ['B', 'C'])
self.addInfo('B', ['D', 'E'])
self.addInfo('C', ['F', 'G'])
self.addInfo('D', ['H', 'I'])
self.addInfo('E', ['J', '.'])
self.addInfo('F', ['K', '.'])
self.addInfo('G', ['.', 'L'])
self.addInfo('H', ['M', '.'])
self.addInfo('I', ['N', '.'])
self.addInfo('J', ['O', '.'])
self.addInfo('K', ['.', '.'])
self.addInfo('L', ['P', '.'])
self.addInfo('M', ['.', '.'])
self.addInfo('N', ['Q', '.'])
self.addInfo('O', ['.', '.'])
self.addInfo('P', ['.', 'S'])
self.addInfo('Q', ['.', '.'])
self.addInfo('R', ['.', '.'])
self.addInfo('S', ['.', '.'])
treeResult = self.postorder('A')
treeAnswer = ['M', 'H', 'Q', 'N', 'I', 'D', 'O', 'J', 'E', 'B', 'K', 'F', 'S', 'P', 'L', 'G', 'C', 'A']
printResultAnswer(name, treeResult, treeAnswer)

f = tg.myTree()
name = "f"
self = f
self.addInfo('A', ['.', 'B'])
self.addInfo('B', ['C', '.'])
self.addInfo('C', ['.', 'D'])
self.addInfo('D', ['E', 'F'])
self.addInfo('E', ['G', '.'])
self.addInfo('F', ['.', 'H'])
self.addInfo('G', ['.', '.'])
self.addInfo('H', ['I', '.'])
self.addInfo('I', ['.', 'J'])
self.addInfo('J', ['K', 'L'])
self.addInfo('K', ['M', '.'])
self.addInfo('L', ['.', 'N'])
self.addInfo('M', ['O', '.'])
self.addInfo('N', ['.', '.'])
self.addInfo('O', ['P', '.'])
self.addInfo('P', ['.', 'Q'])
self.addInfo('Q', ['R', 'S'])
self.addInfo('R', ['.', '.'])
self.addInfo('S', ['.', '.'])
treeResult = self.postorder('A')
treeAnswer = ['G', 'E', 'R', 'S', 'Q', 'P', 'O', 'M', 'K', 'N', 'L', 'J', 'I', 'H', 'F', 'D', 'C', 'B', 'A']
printResultAnswer(name, treeResult, treeAnswer)

h = tg.myTree()
name = "h"
self = h
self.addInfo('A', ['B', 'C'])
self.addInfo('B', ['D', '.'])
self.addInfo('C', ['E', '.'])
self.addInfo('D', ['G', 'F'])
self.addInfo('E', ['H', 'I'])
self.addInfo('F', ['J', '.'])
self.addInfo('G', ['.', 'K'])
self.addInfo('H', ['L', '.'])
self.addInfo('I', ['.', 'M'])
self.addInfo('J', ['.', '.'])
self.addInfo('K', ['.', '.'])
self.addInfo('L', ['.', '.'])
self.addInfo('M', ['.', '.'])
treeResult = self.postorder('A')
treeAnswer = ['K', 'G', 'J', 'F', 'D', 'B', 'L', 'H', 'M', 'I', 'E', 'C', 'A']
printResultAnswer(name, treeResult, treeAnswer)

i = tg.myTree()
name = "i"
self = i
self.addInfo('A', ['B', 'C'])
self.addInfo('B', ['.', '.'])
self.addInfo('C', ['D', 'E'])
self.addInfo('D', ['.', '.'])
self.addInfo('E', ['F', 'G'])
self.addInfo('F', ['.', '.'])
self.addInfo('G', ['H', 'I'])
self.addInfo('H', ['.', '.'])
self.addInfo('I', ['J', 'K'])
self.addInfo('J', ['.', '.'])
self.addInfo('K', ['L', 'M'])
self.addInfo('L', ['.', '.'])
self.addInfo('M', ['.', '.'])
treeResult = self.postorder('A')
treeAnswer = ['B', 'D', 'F', 'H', 'J', 'L', 'M', 'K', 'I', 'G', 'E', 'C', 'A']
printResultAnswer(name, treeResult, treeAnswer)

j = tg.myTree()
name = "j"
self = j
self.addInfo('A', ['.', 'B'])
self.addInfo('B', ['.', 'C'])
self.addInfo('C', ['D', 'E'])
self.addInfo('D', ['.', '.'])
self.addInfo('E', ['.', '.'])

treeResult = self.postorder('A')
treeAnswer = ['D', 'E', 'C', 'B', 'A']
printResultAnswer(name, treeResult, treeAnswer)

printResult(answerCases, wrongCases)
