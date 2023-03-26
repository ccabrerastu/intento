def eje1():
    import array as arr
    a = arr.array('d',[ 1.1, 2.1,3.1])
    a.append(3.4)
    print("Array a = ", a)
    b = arr.array('d',[ 2.1, 3.2, 4.6])
    b.extend([4.5,3.6,7.2 ])
    print("Array b = ", b)
    c = arr.array('d',[ 1.1, 2.1, 3.1])
    c.insert(2,3.4)
    print("Arrays c =", c)
#eje1()
def eje2(): 
    import array as arr 
    a = arr.array('d',[ 1.1, 2.2, 3.8, 3.1, 3.7] )
    print ("Popping last element", a.pop())
    print("Popping 4th element", a.pop(3))
    a.remove(1.1)
    print(a)
#eje2()
def eje3():
    import array as arr
    a = arr.array('d',[ 1.1, 2.1, 3.1, 2.6, 7.8] )
    b = arr.array('d',[ 3.7, 8.6] )
    c = arr.array('d')
    c = a + b
    print ("Array c = ", c)
#eje3()
def eje4():
    import array as arr 
    a = arr.array('d',[ 1.1, 2.1, 3.1, 2.6, 7.8] )
    print(a[0:3])
eje4()
