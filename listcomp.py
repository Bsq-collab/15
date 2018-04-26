'''
Bayan Berri
SoftDev1 pd7
K15
2018-04-25
'''
'''
A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
result will be a new list. resulting from evaluating the expression in the context of the for or if clauses which follow it
'''

UC= "QWERTYUIOPASDFGHJKLZXCVBNM"
lc="qwertyuiopasdfghjklzxcvbnm"
num="1234567890"
na= ".?!&#,;:-_*"

def min_threshold(password):
    caps= [1 for x in password if x in UC]
    lower= [1 for x in password if x in lc]
    nums= [1 for x in password if x in num]
    return len(nums)>=1 and len(lower)>=1 and len(caps)>=1

print min_threshold("1a"); # should be False
print min_threshold("1");# False
print min_threshold("1Ab");#True
print min_threshold("111");#False

def strength_scale(pwd):
    scale=0
    if (len([1 for x in pwd if x in UC])>=1):# if caps increase by 2
        scale+=2
    if (len([1 for x in pwd if x in lc])>=1):# if lower increase by 2
        scale+=2
    if (len([1 for x in pwd if x in num])>=1):# if num increase by 2
        scale+=2
    if (len([1 for x in pwd if x in na])>=1):# if nonalpha increase by 2
        scale+=2
    if (len(pwd)>6):# if nice length increase by 2
        scale+=2
    return scale


print strength_scale("1?baYan...")#10
print strength_scale("123abc")#4
print strength_scale("123AbC")#6
print strength_scale("123AbC...")#10
print strength_scale("a")#2
print strength_scale("1Ab.")#8
