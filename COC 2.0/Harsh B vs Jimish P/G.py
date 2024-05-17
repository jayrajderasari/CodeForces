# def inlt():
#     return(list(map(int,input().split())))
# # 1 2 3
# # [1, 2, 3]

# def relative_sort_array(arr1, arr2):
#   index_map = {}
#   for i, elem in enumerate(arr1):
#     index_map[elem] = i
#   arr2.sort()
#   sorted_arr = []
#   for elem in arr2:
#     sorted_arr.append(arr1[index_map[elem]])
#   return sorted_arr

# n = int(input())
# p = inlt()
# a = inlt()
# b = inlt()
# j = int(input())
# c = inlt()

# # for i in range(n):
# #     if a[i] in d:
# #         d[a[i]].append(p[i])
# #     else:
# #         d[a[i]] = [p[i]]
# #     if b[i] in d:
# #         d[b[i]].append(p[i])
# #     else:
# #         d[b[i]] = [p[i]]
# ans = []
# # for co in c:
# #     if d[co]:
# #         cost = min(d[co])
# #         ans.append(cost)
# #         for z in range(len(p)):
# #             if p[z]==cost:
# #                 d[a[z]].remove(cost)
# #                 d[b[z]].remove(cost)
# #                 break        
# #     else:
# #         ans.append(-1)

def find_cheapest_tshirt(tshirts, buyer_color, bought_tshirts):
    for i, (price, front_color, back_color) in enumerate(tshirts):
        if i not in bought_tshirts and (front_color == buyer_color or back_color == buyer_color):
            bought_tshirts.add(i)
            return price
    return -1

def compute_prices(tshirts, buyers):
    tshirts.sort()  # Sort t-shirts based on prices
    bought_tshirts = set()  # Keep track of bought t-shirts
    prices = []

    for buyer_color in buyers:
        price = find_cheapest_tshirt(tshirts, buyer_color, bought_tshirts)
        prices.append(price)

    return prices

# Read input
n = int(input())
tshirt_prices = list(map(int, input().split()))
tshirt_colors_front = list(map(int, input().split()))
tshirt_colors_back = list(map(int, input().split()))

tshirts = list(zip(tshirt_prices, tshirt_colors_front, tshirt_colors_back))

m = int(input())
buyers = list(map(int, input().split()))

# Compute prices
result_prices = compute_prices(tshirts, buyers)

for i in result_prices
