from typing import List

"""
Using a hash map or dictionary is often a good way to solve problems.

For problems that require mapping items to how many times they appear in an array,
a dictionary is a quick look up in constant time.

However, the tradeoff is space complexity, since an entirely new data structure
needs to be built to store the data for lookups.
"""


def sort_scores(
    unsorted_scores: List[float], highest_possible_score: float
) -> List[float]:
    """
    Ex. 1
    input: unsorted_scores = [37, 89, 41, 65, 91, 53], highest_possible_score = 100
    output: [91, 89, 65, 53, 41, 37]

    Requirements:
    - Must be faster than O(n log n) time
    - i.e., try for O(n) time!

    Questions:
    Q: Can multiple players have the same score?
    A: Yes! Example [81, 81, 10, 2, 2]
    """
    sorted_scores = []

    scores_count = [0] * (highest_possible_score + 1)

    # Iterate through scores and generate a list with index representing
    # the score itself, and the value representing the number of times it
    # appears in the list.
    for score in unsorted_scores:
        scores_count[score] += 1

    for score in range(len(scores_count) - 1, -1, -1):
        count = scores_count[score]
        for _ in range(count):
            sorted_scores.append(score)

    return sorted_scores


print(
    "sort_scores([37, 89, 41, 65, 91, 53], 100) = "
    + str(sort_scores([37, 89, 41, 65, 91, 53], 100))
)
