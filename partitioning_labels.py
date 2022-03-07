

def partition(string):
    # time complexity: O(n)
    # space complexity: O(1)
    last = {}
    results = []
    start = 0
    end = 0

    for i in range(len(string)):
        last[s[i]] = i

    for i in range(len(string)):
        index = last[s[i]]
        if index > end:
            end = index
        elif i == end:
            results.append(s[start:end+1])
            start = end = end + 1

    return results


def partition_refactored(string):
    # time complexity: O(n)
    # space complexity: O(1)
    last = {c: i for i, c in enumerate(string)}
    results = []
    start = 0
    end = 0

    for i, c in enumerate(string):
        end = max(last[c], end)
        if i == end:
            results.append(s[start:end+1])
            start = end + 1

    return results


if __name__ == "__main__":
    s = "ababcbacadefegdehijhklij"
    print(partition(s))
    print(partition_refactored(s))
