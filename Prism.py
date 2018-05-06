#Our_Python_P265
class MyClass2:
    def __init__(self):
        self.value = 0
        print("This is __init__() module !!")

#Our_Python_p267
class Prism:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def content(self):
        return self.width*self.height*self.depth
'''Pythonのインタラクティブで
    import Prism
    p1 = Prism.Prism(a,b,c)
    p1.content
でa*b*cの答えが出てくる
p1は任意の変数
参考：https://docs.python.jp/3/tutorial/modules.html
'''
