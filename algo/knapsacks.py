from decimal import Decimal


class Item:

    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        
    def __str__(self):
        return 'Item weight: {}, value: {}'.format(self.weight, self.value)
    
    def __repr__(self):
        return self.__str__()


def fractional_knapsack_greedy(items, max_weight_allowed):
    if items and len(items) > 0 and max_weight_allowed > 0:
        capacity_remaining = max_weight_allowed
        optimal_value = 0
        items_sorted_greedily = sorted(items, key=lambda item: Decimal(item.value) / Decimal(item.weight), reverse=True)
        for item in items_sorted_greedily:
            item_fraction = 1.0 if item.weight <= capacity_remaining else Decimal(capacity_remaining) / Decimal(item.weight)
            optimal_value += item.value if item_fraction == 1.0 else (item.value * item_fraction) 
            capacity_remaining -= item.weight if item.weight <= capacity_remaining else capacity_remaining
            if capacity_remaining == 0:
                break
        return "{:.2f}".format(optimal_value)
    return 0
        

def knapsack_with_repetition(items, max_weight_allowed):
    if items and len(items) > 0 and max_weight_allowed > 0:
        optimal_values = [0] * (max_weight_allowed + 1)
        for temp_max_weight_allowed in range(1, max_weight_allowed + 1):
            items_eligible = filter(lambda item: item.weight <= temp_max_weight_allowed, items)
            if items_eligible:
                optimal_values[temp_max_weight_allowed] = max([optimal_values[temp_max_weight_allowed - item.weight] + item.value for item in items_eligible])
        return optimal_values[max_weight_allowed]
    return 0


def knapsack_without_repetition(items, max_weight_allowed):
    if items and len(items) > 0 and max_weight_allowed > 0:
        __reorganize_items(items)
        optimal_values = [[0 for _ in range(len(items))] for j in range(max_weight_allowed + 1)]
        for j in range(1, len(items)):
            for w in range(1, max_weight_allowed + 1):
                optimal_values[w][j] = max(optimal_values[w - items[j].weight][j - 1] + items[j].value,
                                           optimal_values[w][j - 1]) if items[j].weight <= w else optimal_values[w][j - 1]
        return optimal_values[max_weight_allowed][len(items) - 1]
    return 0


def __reorganize_items(items):
    if items and len(items) > 0:
        items.append(0)
        counter = len(items) - 1
        while(counter > 0):
            items[counter] = items[counter - 1]
            counter -= 1
        items[counter] = None


if __name__ == '__main__':
    items = [Item(10, 60), Item(40, 40), Item(20, 100), Item(30, 120)]
    
    print fractional_knapsack_greedy(items, 50)    
    print knapsack_with_repetition(items, 50)
    print knapsack_without_repetition(items, 50)
