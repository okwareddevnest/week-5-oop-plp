from magazine import Magazine

mag = Magazine("Python for All", "Guido van Rossum", 2020)

print(mag.get_details())         
print(mag.borrow())          # Overrides the original method
