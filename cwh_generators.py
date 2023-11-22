
#generators in python - they are a special type of function that provides output like list but does not store it

def my_generator():
    for i in range(5000):
        yield i

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))

for i in gen:
    print(i)
