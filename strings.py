hello = 'hello world'
print(hello)
run = "I'm going on a run" #using '
print(run)
print('hello \nworld')
print( len(hello) )

print( hello[0])
print( hello[-3])

print( hello[6:])
print(hello[6:9])
print(hello[:5])

print( hello[::2] )

print(hello[:5] + ' ' + hello[6:])
letter = 'z'
print(letter * 10)

print(hello.replace('l', 'L'))
print( hello.upper())
print( hello.split('o'))

title = 'Hi {0} welcome to our hotel. Have a lovely {1}'
print ( title.format('Sonia', 'Friday'))

title = 'Hi2 {name} welcome to our hotel. Have a lovely {day}'
print ( title.format(name='Sonia', day='Friday'))