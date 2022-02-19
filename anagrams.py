import collections

word = ["eat","tea","tan","ate","nat","bat"]


def group_anagrams(strs):
    ans = collections.defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return ans.values()


print(group_anagrams(word))