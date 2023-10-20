def read_input():
    input_data = input().split()
    piece = input_data[0]
    quantity, value = [float(v) for v in input_data[1:]]
    return piece, quantity, value


piece1, quantity1, value1 = read_input()
piece2, quantity2, value2 = read_input()

total = quantity1 * value1 + quantity2 * value2

print(f"VALOR A PAGAR: R$ {total:.2f}")
