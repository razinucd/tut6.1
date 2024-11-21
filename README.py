# tut6.1

def f (x):
   y=-(x ** 2) + (3 * x) - 2 # the formula we need to do the process on
   return y

x = 1
while x<=2 and x>=1:
    print (" when x =", x , "f(x)=", f(x))
    x += 0.1
mid= f(1.10)+ f(1.20)+f(1.30)+f(1.40)+f(1.50)+f(1.60)+f(1.70)+f(1.80)+f(1.90) # provides the middle sum

integ= (0.1/2)*(2*(mid))
trueaprox= (1/6) - integ
true= 1/6
final= (trueaprox/true) * 100 # finds the final percentage of error
print(" the first height is: ", f(1))
print(" the last height is: ", f(2))
print (" the middle sum is", mid)
print (" integration is approx.: " , integ)
print ("the value of integration is: 1/6 ")
print ("the error  is " , final , " %")
