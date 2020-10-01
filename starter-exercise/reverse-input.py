#Reverse Input
def reverse_txt(parameter):
    new = ''
    for i in parameter:
        new = i + new
    return new

msg = input("enter text\n")
print(reverse_txt(msg))
