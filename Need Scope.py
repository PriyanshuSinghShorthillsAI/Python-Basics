# example_scope_importance.py

# Global variable
global_var = "I am a global variable"

def function_with_local_scope():
    """
    Demonstrates local scope.
    """
    local_var = "I am a local variable"  # Local to this function
    print(local_var)

def function_with_global_scope():
    """
    Demonstrates the use of global scope.
    """
    global global_var  # Refers to the global variable
    global_var = "Global variable modified"  # Modifies the global variable
    print(global_var)

def outer_function():
    """
    Demonstrates nonlocal scope.
    """
    outer_var = "I am an outer variable"

    def inner_function():
        nonlocal outer_var  # Refers to the variable in the enclosing scope
        outer_var = "I modified the outer variable"  # Modifies the outer variable
        print(outer_var)

    inner_function()
    print(outer_var)  # Shows the modified value

if __name__ == "__main__":
    print("Demonstrating Local Scope:")
    function_with_local_scope()
    # Uncommenting the next line would raise an error as local_var is not accessible here
    # print(local_var)  

    print("\nDemonstrating Global Scope:")
    print(f"Before global function call: {global_var}")
    function_with_global_scope()
    print(f"After global function call: {global_var}")

    print("\nDemonstrating Nonlocal Scope:")
    outer_function()
