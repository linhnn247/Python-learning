##a
n = int(input('number of asterisk? '))
print(n*"*")
##b
n = int(input('number of x and asterisk? '))
print(n*"x*")
##c
print()
##d
r = int(input('number of stars in a row? '))
c = int(input('number of stars in a column? '))
if c % 2 == 0:
    print(c/2*(r*"x*" + '\n'+ r*"*x" + '\n'))
else:
    c1 = c//2
    print(c1*(r*"x*" + '\n'+ r*"*x" + '\n'),end="")
    print(r*"x*" + '\n')




