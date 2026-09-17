read = 1
write = 2
Execute = 4

permission = read | write
print("Permission value:" , permission)

if permission & read:
    print("Read permission is available. ")
if permission & write:
    print("Write permission is available. ")
if permission & Execute:
    print("Execute permission is available. ")
    