from math import *
print("Fanning - friction - factor")

while True:
    operation = input("Enter operation: ").lower()
    if operation == "ff":
        Re = float(input("Enter Reynold Number: "))
        E = float(input("Enter Pipe relative roughness: "))
        last_bracket = ((E ** 1.1098) / 2.8257) + ((7.149 / Re) ** 0.8981)
        left_side = -((5.0452 / Re) * log10(last_bracket))
        right_side = E / 3.7065
        result_from_brackett = right_side + left_side
        print(f"result_from_brackett: {result_from_brackett}")
        inverse_root = -4 * log10(result_from_brackett)
        print(inverse_root)
        fanning_factor = pow((1 / inverse_root), 2)
        print(f"fanning_factor: {fanning_factor}")
    elif operation == "dp":
        ff = float(input("Enter fanning friction factor: "))
        p = float(input("Enter density(lb/ft^3): "))
        u = float(input("Enter velocity flow rate(ft/sec): "))
        l = float(input("Enter the length(ft): "))
        D = float(input("Enter the pipe diameter(in): "))
        pressure_drop = (2 * ff * p * pow(u, 2) * l) / (32.17 * D / 12)
        print(pressure_drop)
