

def unique_bst(n):
    # initialize 0 to n sum_trees
    # if n = 3
    # need to store answers from G(0), G(1), G(2), and G(3)
    sum_trees = [1] * (n + 1)

    for nodes in range(2, n + 1):
        total = 0
        for root in range(1, nodes + 1):
            left = root - 1
            right = nodes - root
            total += sum_trees[left] * sum_trees[right]
        sum_trees[nodes] = total

    return sum_trees[n]


if __name__ == "__main__":
    print(unique_bst(6))
