def greet(input):
    if "Hello" in input:
        return "Hello there"
    else:
        return "Im not sure what you meant"

greeting = greet("Hello, Computer")
print("Hm " + greeting)
