def total_fruit(tree):
    i = j = -1
    counter = result = 0
    for k, fruit in enumerate(tree):
        if i == -1:
            i = fruit
        if fruit != i and j == -1:
            j = fruit
        if fruit in (i, j) or (fruit == i and j == -1):
            counter += 1
            result = max(result, counter)
        else:
            counter = 1
            j = fruit
            i = tree[k - 1]
            l = k - 1
            while tree[l] == i:
                counter += 1
                l -= 1
    return result


if __name__ == '__main__':
    tree = [1,2,1]
    print total_fruit(tree)
