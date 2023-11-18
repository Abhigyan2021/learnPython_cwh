
#calculator command - prints output of simple arithmetic expression

'''
Rules:
1. Do not give any random symbol or alphabet - That gives an error.
2. 1234567890 - Are digits
3. + is addition
4. - is subtraction
5. * is multiplication
6. / is float division(with decimal points)
7. // is integer division(without decimal points)
8. Do not give spaces between two digits of a number - That gives an error
9. Do not run this file by double clicking, Use the command prompt or terminal to run it.
'''

try:
    import sys #stdlib
#Exception and Error Handling
except ImportError as e:
    print("Module - 'sys' could not be imported from stdlib!")

try:
    print(eval(" ".join(sys.argv[1:]))) #Evaluate the given expression and print the result out.
#Exception and Error Handling
except Exception as e:
    print("Expression could not be validated or evaluated.")
    print("1. Make sure that you typed the expression correctly.")
    print("2. Make sure that there are no spaces between 2 digits of a number.")
    print("And try again.")
    print(f"Details about the error: {e}")
    
