#1st exercies
import statistics as s
numbers = [ int(input()) for i in range(3) ]
print("{:.6f}; {:.6f}; {:.6f}; {:.6f}".format(s.fmean(numbers), s.harmonic_mean(numbers), s.median(numbers), max(numbers) ** min(numbers) / s.mean(numbers)))                   # output all abrakadabry with thanks to statisticks module

#2nd exercies
name = input()  # entering user name
age = input()   # entering his age
print('Hello, ', name,', with age ', age ,sep = '')  # o

#3rd excercies
n = int(input())
print(n // 60 , n % 60,sep = '\n')
