# Write a program that prints the integers from 1 to 100,
# but for multiples of 3 print ‘FIZZ’ instead of number and for multiples of five print ‘BUZZ’.
# For numbers which are multiples of both 3 and 5 print ‘FIZZBUZZ’.

for i in range(1,101):
    if i%15 == 0:
        print('FIZZ')
    elif i%5 == 0:
        print('BUZZ')
    elif i%3 == 0:
        print('FIZZBUZZ')
    else:
        print(i)
    

