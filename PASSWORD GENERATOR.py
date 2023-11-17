import random
#importing random library

password="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz!@#$%&*.,:?"
#creating a variable with all the possible combinations string

length=int(input('Enter the length of password :'))
#taking length as an input

output="".join(random.sample(password,length))
#assigning all the random string together to a variable

print(f'the password is {output}')
#printing the output