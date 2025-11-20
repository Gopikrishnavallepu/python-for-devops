def outer_function():
    x = 10 # Enclosing variable
    def inner_function():
        nonlocal x # Modify the enclosing variable
        x = 20
        print("Inner:", x)
    inner_function()
    print("Outer:", x)
outer_function()