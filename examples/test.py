__author__ = 'Xinyue'
from cvxpy import *
import dccp
from dccp.problem import is_dccp

x = Variable(2)
y = Variable(2)
myprob = Problem(Maximize(norm(x-y,2)), [0<=x, x<=1, 0<=y, y<=1])
print "problem is DCP:", myprob.is_dcp()   # false
print "problem is DCCP:", is_dccp(myprob)  # true
result = myprob.solve(method = 'dccp')
print "========================"
print "x =", x.value
print "y =", y.value
print "cost value =", result[0]

