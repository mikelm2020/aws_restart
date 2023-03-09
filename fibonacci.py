
fibonacci_list = [0,1]
for i in range(10):
    if i == 0 or i == 1:
        continue
    next_secuence = fibonacci_list[i-1] + fibonacci_list[i-2]
    fibonacci_list.append(next_secuence)

print(fibonacci_list)
    
