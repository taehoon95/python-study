power = lambda x: x * x
under_3 = lambda x: x < 3

list_input_a = [1,2,3,4,5]

output_a = map(lambda x: x * x,list_input_a)
print(list(output_a))

output_b = filter(lambda x: x < 3,list_input_a)
print(list(output_b))

output_c = lambda x,y : x * y
res = output_c(5,3)
print(res)