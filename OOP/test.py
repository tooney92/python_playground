# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def oldest_cat(cls, *argv):
#         obj = list(filter(lambda x: x.age == max(list(map(lambda x: x.age,argv))), argv))[0]
#         return f"{obj.name} is the oldest with an age of {obj.age}"



# cat1 = Cat("pepe", 23)
# cat2 = Cat("lele", 45)
# cat3 = Cat("ele", 99)
# cat4 = Cat("dele", 67)

# print(Cat.oldest_cat(cat3, cat2, cat1, cat4))
# print(cat2.)

# def myFun(arg1, *argv): 
#     # print ("First argument :", arg1) 
#     bask = []
#     for arg in argv: 
#         bask.append(arg)
#     print(bask)
  
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks') 


# li = [1, 2, 3, 4]
# test  = filter(lambda x: x<4, li)
# print(list(test))

test = [1, 2, 1,1,1, 0, 5, 1,4,4,4,3, 6, 10, 8]
# test = [1000, 12000, 5000,0,0,0,0,0,0,0,0,0,0,90, 1000, 7000, 600, 400, 500, 500, 4000, 3000, 1000]
def pivot(sample, length):
    for i in range(1, length-1):
        if sum(sample[0:i]) == sum(sample[i+1:]):
            return i
    return -1

print(pivot(test, len(test)))


'''
test = [1000, 12000, 5000,0,0,0,0,0,0,0,0,0,0,90, 1000, 7000, 600, 400, 500, 500, 4000, 3000, 1000]
def pivot(sample, length):
    for i in range(1, length-1):
        if sum(sample[0:i]) == sum(sample[i+1:]):
            return (sample[i], "is the pivot with an index position of:", i)
        # print(sum(sample[0:i]),f"<--{sample[i]}-->",sum(sample[i+1:]))
    return ("none")

print(pivot(test, len(test)))

'''