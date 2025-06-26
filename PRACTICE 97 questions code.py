#question 5
x = 10
y =20 
print(id(x)) #140723810085592
print(id(y)) # 140723810085912
x,y = y,x
print(x)
print(y) #20 10
print(id(x)) #140723810085912
print(id(y)) #140723810085592 ;address is also swapped

#question 20
l= ['p','r','i','y','a','n','k','a']
l1 = len(l)
s= " ".join(l)
print(l1) # 8
print(s) # p r i y a n k a

#question 31
list1 = ['a','b','g',1,5]
print(list1.pop())  # 5

#question 33
var = 2
print(2==2.0) #True

#question 38
print(str(True),int('4'),end=" ") #True 4
# int('4.5') # string should not be float value
print(int('6'))


#question 51
s= range(5)
print(type(s)) #range

#question 54
str='python'
print(type(str)) #str

#question 56
f=3.14
print(type(f))  #float


#question 58
x = 10
y= '20'
# print(x+y) #TypeError: unsupported operand type(s) for +: 'int' and 'str'

#question 69
x=[1,2,3]
y=x.copy()
x.append(4)
print(y) # [1, 2, 3]

#question 78
x= 'hello'
y= x.replace('l','L',1)
print(y) # it will replace small letter 'l' with capital 'L' only 1 letter; heLlo

#question 82
x=[1,2,3]
y= x[:]
x[0]=4
print(y) #[1,2,3]

#question 91
age = 25
print("my age is:",age)  #my age is: 25

#question 92
number= [1,2,3,4,5]
number[-1]=20
print('the edited list is',number,'the edited element is',number[-1]) # the edited list is [1, 2, 3, 4, 20] the edited element is 20

#question 94
a=23
b=20
sum = a+b
print("the sum of {} and {} is {}".format(a,b,sum)) #the sum of 23 and 20 is 43

#question 95
length = 76
width =45
area = length * width
print('the area of rectangle is',area) # the area of rectangle is 3420

#question 96
radius= 8.9
pi=3.14
area= pi*radius**2
print('the area of the circle is',area,'and the rounded value is',round(area,2)) # the area of the circle is 248.71940000000004


#question 97
a= "Learning"
b= "is fun !!"
s= a+" "+b
print(s) #Learning is fun !!


 