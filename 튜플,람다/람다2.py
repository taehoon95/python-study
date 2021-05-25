def power(item):
    return item * item


def under_3(item):
    return item < 3

list_input_a = [1, 2, 3, 4, 5]

#map함수
output_a = map(power, list_input_a)
print(list(output_a))

output_b = filter(under_3, list_input_a)
print(list(output_b))

