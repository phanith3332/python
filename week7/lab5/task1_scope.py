# task1_scope.py

# Global variable
counter = 0
def show_local():
    # Local variable
    counter = 10
    print("Local counter:", counter)
# Call the function
show_local()
# Access the global variable
print("Global counter:", counter)

'''output:
Local counter: 10
Global counter: 0'''
