'''
i searched this site(https://thispointer.com/python-how-to-use-if-else-elif-in-lambda-functions/) to check
how to use conditional in lambda functions. to do this, you first create a lambda function. (1) returns a
"_" if (2) executes to true. {we will presume x is "w"}. (6) is the else statement that lambda requires whenver we use an if
. sadly we cannot employ elif statments. so to deal with this, inside (6), we can nest another set of if and else as we did in
(3). the inner else, we can pass in another if and else as we did in (4) and (5)  
lambda x : "_"(1) if x == "w"(2) else("/" if x == "c"(3) else("/n" if x == "d"(4) else " "(5) ))(6)
lambda x : "_" if x == "w" else ("/" if x == "c" else ("/n" if x == "d" else " ")). 
so techincally we have sets of ifs and else's. 

lesson: I learnt improved my understanding of how to use lambda and maps. I also got a proper understanding of joins and splits. 
both codes do the same thing, but the power of lambda and higher functions can be seen in the latter. i have written 4 codes that
do the same thing. 


'''
def hill_ish(command):
    transComm = []
    for char in command:
        if char == "w":
            transComm.append("_(w)")
        elif char == "c":
            transComm.append("/(c)")
        elif char == "d":
            transComm.append("\n(d)")
        elif char == " ":
            transComm.append(" (j)")
        else:
            pass
    return "".join(transComm)
    # return transComm

print(hill_ish("wwwwwwwwwwcdcdcd     "))


print()
print("--------------------------------------------\n--------------------------------------------1")
print()


def hill_ish(command):
    test = lambda x : "_(w)" if x == "w" else ("/(c)" if x == "c" else ("\n(d)" if x == "d" else " (j)"))
    return "".join(list(map(test, command)))

print(hill_ish("wwwwwwwwwwcdcdcd     "))

print()
print("--------------------------------------------\n--------------------------------------------2")
print()

def hill_ish(command):
    return "".join(list(map(lambda x : "_(w)" if x == "w" else ("/(c)" if x == "c" else ("\n(d)" if x == "d" else " (j)")), command)))

print(hill_ish("wwwwwwwwwwcdcdcd     "))
print("--------------------------------------------\n--------------------------------------------3")


def hill_ish(command):
    transComm = []
    test = lambda x : "_(w)" if x == "w" else ("/(c)" if x == "c" else ("\n(d)" if x == "d" else " (j)"))
    for char in command:
        transComm.append(test(char))    
    return "".join(transComm)

print(hill_ish("wwwwwwwwwwcdcdcd     "))


print()
print("--------------------------------------------\n--------------------------------------------4")
print()


'''
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def oldest_cat(cls, *argv):
        obj = list(filter(lambda x: x.age == max(list(map(lambda x: x.age,argv))), argv))[0]
        return f"{obj.name} is the oldest with an age of {obj.age}"



cat1 = Cat("pepe", 23)
cat2 = Cat("lele", 45)
cat3 = Cat("ele", 99)
cat4 = Cat("dele", 67)

print(Cat.oldest_cat(cat3, cat2, cat1, cat4))
print(cat2.)

----------------------------------------------------------------
# sample = [1, 2, 3, 0, 5, 1,4,4,4,3, 6, 10, 8]
test = [1,2,0,3]
def pivot(sample):
    for i in range(1, len(sample)-1):
        if sum(sample[0:i]) == sum(sample[i+1:]):
            return (sample[i], "is the pivot with an index position of:", i)
    return ("none")
    # print(sum(sample[0:i]),f"<--{sample[i]}-->",sample[i+1:len(sample)])
    # print(sample[0:i],f"<--{sample[i]}-->",sample[i+1:])


print(pivot(test))

'''