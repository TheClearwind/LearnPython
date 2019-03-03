class Course:
    language='zh'
    def __init__(self):
        pass

print(Course.language)
Course.language='en'#类中静态属性可以这样更改
print(Course.language) 
#Course.__dict__['language']='zh' #类中静态属性不可以这样更改
print(Course.language)
#类与对象单向连接，对象可以看类的属性，类不可以看对象的