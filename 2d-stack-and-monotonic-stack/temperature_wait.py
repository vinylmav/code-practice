temps = [73, 74, 75, 71, 69, 72, 76, 73]

def temperature_wait(temps):
    stack = [(temps[0], 0)]
    answer = [0]*len(temps)
    for i in range(1, len(temps)):
        temp = temps[i]
        while stack and stack[-1][0] < temp:
            answer[stack[-1][1]] = i - stack[-1][1]
            stack.pop()
        stack.append((temp, i))
    return answer

print(temperature_wait(temps))
