import heapq
# return the kth largest number

nums = [5, 7, 8, 3, 6, 1, 4]
k = 4
ans = []

for num in nums:
    if len(ans) < 4:
        heapq.heappush(ans, num)
    else:
        heapq.heappushpop(ans, num)

smallest = ans[0]
for num in ans:
    if num < smallest:
        smallest = num


print(smallest)
