class people:
    ###__init__用于设置中实例的属性，即最初在创造实例时需要赋值的属性
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    ###除__init__方法以外的方法，一般都用于对实例和属性的操作
    def speak(self):
        print ('Hello, my name is %s, and I\'m %d years old'  % (self.name, self.age))
        
##创建实例，并赋值属性
Angle = people('Angle', 28)
##对实例和属性的操作
Angle.age
Angle.speak()

##计算点之间距离的案例
class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    
    def __getX__(self):
        return self.x
    def __getY__(self):
        return self.y

#
class Line:
    ##创建实例和属性，属性不一定是一开始就赋予的
    def __init__(self, p1, p2):
        self.x = (p1.x - p2.x)** 2
        self.y = (p1.y - p2.y)** 2
        self.line = round((self.x + self.y)**0.5, 2)
    
    ##函数？方法？
    def getLen(self):
        return self.line
    
    def __getLen1__(self):
        return self.line
    
    ## 这样子不能得到想要的输出。
    def __getLen2__(self):
        return round((self.x + self.y)**0.5, 2)

p1 = Point(1,1)
p2 = Point(5,8)
line = Line(p1, p2)
line.__getLen__()