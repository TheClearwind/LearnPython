class A:
    def func(self):
        print(type(self)) #B
        print("父类func")
class B(A):
    def func(self):
        #A.func(self) 
        super().func() #等价于A.func(self)
        print("子类func")


b=B()
b.func()
print(b.__dict__)