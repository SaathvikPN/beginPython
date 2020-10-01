#Reverse Input
def reverse_txt(parameter):
    new = ''
    for i in parameter:
        new = i + new
    return new

msg = input("enter text\n")
print(reverse_txt(msg))


#For Palindrome 
'''
#Reverse Input
def reverse_txt(parameter):
    new = ''
    for i in parameter:
        new = i + new
    return new

msg = input("enter text\n")
if reverse_txt(msg)==msg:
    print(msg,"is Palindrome")
else:
    print(msg,": NOT a palindrome")
'''
