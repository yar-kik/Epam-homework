"""
Task 2_3

You are given n bars of gold with weights: w1, w2, ..., wn and bag with capacity W.
There is only one instance of each bar and for each bar you can either take it or not
(hence you cannot take a fraction of a bar). Write a function that returns the maximum weight of gold that fits
into a knapsack's capacity.

The first parameter contains 'capacity' - integer describing the capacity of a knapsack
The next parameter contains 'weights' - list of weights of each gold bar
The last parameter contains 'bars_number' - integer describing the number of gold bars
Output : Maximum weight of gold that fits into a knapsack with capacity of W.

Note:
Use the argparse module to parse command line arguments. You don't need to enter names of parameters (i. e. -capacity)
Raise ValueError in case of false parameter inputs
Example of how the task should be called:
python3 task3_1.py -W 56 -w 3 4 5 6 -n 4
"""
from argparse import ArgumentParser


def bounded_knapsack(W: int, w: list, n: int) -> int:
    """
    Function that returns the maximum weight of gold that fits into a bounded
    knapsack.
    @param W: The capacity of a knapsack.
    @param w: List of weights of each gold bar.
    @param n: The number of gold bars.
    @return: Maximum weight of gold that fits into a knapsack.
    """
    if W <= 0 \
            or n <= 0 \
            or any([item for item in w if item <= 0]) \
            or len(w) != n:
        raise ValueError

    # grouped_items = [(w[i], n) for i in range(len(w))]
    # items = sum(([wt] * n for wt, n in grouped_items), [])
    items = w
    table = [[0 for w in range(W + 1)] for j in range(len(items) + 1)]
    for j in range(1, len(items) + 1):
        wt = items[j - 1]
        for w in range(1, W + 1):
            if wt > w:
                table[j][w] = table[j - 1][w]
            else:
                table[j][w] = max(table[j - 1][w],
                                  table[j - 1][w - wt] + wt)
    result = []
    w = W
    for j in range(len(items), 0, -1):
        was_added = table[j][w] != table[j - 1][w]

        if was_added:
            wt = items[j - 1]
            result.append(items[j - 1])
            w -= wt
    return sum(result)


def main():
    parser = ArgumentParser(description="Program can calculate maximum weight"
                                        "of gold that fits into a knapsack"
                                        "with entered capacity")
    parser.add_argument("-W", type=int,
                        help="Integer describing the capacity of a knapsack")
    parser.add_argument("-w", type=int, nargs="*",
                        help="List of weights of each gold bar")
    parser.add_argument("-n", type=int,
                        help="Integer describing the number of gold bars")
    args = parser.parse_args()
    print(bounded_knapsack(args.W, args.w, args.n))


if __name__ == '__main__':
    main()
