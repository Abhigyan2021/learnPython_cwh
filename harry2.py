

def welcome():
    print("hey, you are welcome from Harry!")

#without if __name__ = '__main__': it will be executed twice hence it is necessary

print(__name__)

if __name__ == "__main__":
    welcome()