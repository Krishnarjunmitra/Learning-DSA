"""
Greedy Algorithms: Theory and Implementation
"""

def coin_change(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
    return count if amount == 0 else -1

def activity_selection(activities):
    activities.sort(key=lambda x: x[1])
    last_end = -1
    count = 0
    for start, end in activities:
        if start >= last_end:
            count += 1
            last_end = end
    return count

'''
Use Cases:
- Coin change problem
- Activity selection
- Huffman coding
- Minimum spanning tree (Prim, Kruskal)
'''
