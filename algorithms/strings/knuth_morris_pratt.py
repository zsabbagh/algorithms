from typing import Sequence, List

def knuth_morris_pratt(text : Sequence, pattern : Sequence) -> List[int]:
    """
    Given two strings text and pattern, return the list of start indexes in text that matches with the pattern
    using knuth_morris_pratt algorithm.

    Args:
        text: Text to search
        pattern: Pattern to search in the text
    Returns:
        List of indices of patterns found

    Example:
        >>> knuth_morris_pratt('hello there hero!', 'he')
        [0, 7, 12]

    If idx is in the list, text[idx : idx + M] matches with pattern.
    Time complexity of the algorithm is O(N+M), with N and M the length of text and pattern, respectively.
    """
    branches = set()

    n = len(text)
    m = len(pattern)
    pi = []
    for i in range(m):
        branches.add(1)
        pi.append(0)
    i = 0
    j = 0
    # making pi table
    for i in range(1, m):
        branches.add(2)
        while j and pattern[i] != pattern[j]:
            branches.add(3)
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            branches.add(4)
            j += 1
            pi[i] = j
        else:
            branches.add(5)
    # finding pattern
    j = 0
    ret = []
    for i in range(n):
        branches.add(6)
        while j and text[i] != pattern[j]:
            branches.add(7)
            j = pi[j - 1]
        if text[i] == pattern[j]:
            branches.add(8)
            j += 1
            if j == m:
                branches.add(10)
                ret.append(i - m + 1)
                j = pi[j - 1]
            else:
                branches.add(11)
        else:
            branches.add(9)
    with open('data/branch-coverage', 'a') as f:
        function_name = "knuth_morris_pratt"
        total_branches = 11
        ratio = str(len(branches) / total_branches)
        f.write(
            f'{function_name},{total_branches},{ratio},'
        )
        branches_not_found = ""
        for i in range(1, int(total_branches) + 1):
            if i not in branches:
                branches_not_found += f"{str(i)};"
        if branches_not_found == "":
            f.write("0")
        else:
            branches_not_found.strip(";")
            f.write(branches_not_found)

        f.write('\n')
    return ret
