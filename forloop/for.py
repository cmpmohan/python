
Write a Python program to construct the following pattern

`*` 

`* *`

`* * *`

`* * * *` 

`* * * * *` 

`* * * *` 

`* * *` 

`* *` 

`*`

Solution:

for i in range(1,6):
 print('*' * i)
for l in range(1,6):
 print('*' * (5-l) )
