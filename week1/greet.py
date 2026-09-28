import sys
if len(sys.argv) > 1:
    name = sys.argv[1]
    print(f"Hello, {name}!")
else:
    print("Usage: python greet.py <name>")
    
    #output:Usage: python greet.py <name>