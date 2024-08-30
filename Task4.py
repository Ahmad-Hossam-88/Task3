num, maxWeight = map(int, input().split())
items = []
for i in range(num):
    weight, value = map(int, input().split())
    items.append([weight, value])
items.sort(key=lambda item: item[1] / item[0], reverse=True)
valueSum, weightSum = 0, 0
for item in items:
    if item[0] + weightSum <= maxWeight:
        weightSum += item[0]
        valueSum += item[1]
    else:
        continue
print(valueSum)

# Wrong answer
