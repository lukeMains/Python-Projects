count = int(input('How many pythagorean triples would you like to see? '))

l = 1
m = 2
n = 1

print('x\ty\tz\t')
for i in range(count):
    x = l*(m*m - n*n)
    y = 2*l*m*n
    z = l*(m*m + n*n)
    
    print(x, y, z, sep='\t')

    m += i+1
    n += i+1
