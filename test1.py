next_input = 0
inputs = []
while True:
 next_input = input('Please enter a number:')
 if next_input == -1:
    break
 else:
    inputs.append(next_input)

print(sum(inputs) / len(inputs))