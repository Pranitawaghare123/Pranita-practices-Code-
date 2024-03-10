from array import *
vals =array("i",[2,4,3,5,6])
print(vals)
print(vals.buffer_info())
print(vals.typecode)
# vals.reverse()
# print(vals)
# print(vals[2])
# for i in range (5):
#     print(vals[i])
# for i in range(len(vals)):
#     print(vals[i])

# for i in vals:
    # print(i)

val=array('u',['a','c','f','d'])
val1=array(vals.typecode,(a*a for a in vals))
for i in val1:
    print(i)