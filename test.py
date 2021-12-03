class Test:
    def __init__(self):
        pass
    def set(self, point):
        self.point = point
    def get(self):
        return self.point

a = Test()
a.set(1)
print(a.get())
print(a.point)

b = Test()
b.set(2)
print(b.get())
print(b.point)
