"""Exact finite checks supporting the Appendix A source audit.

These checks do not compile Lean and do not prove the statements for arbitrary n.
Run with Python 3.10 or later; no third-party dependency is required.
"""

from functools import lru_cache
import json


def main():
    results = []
    for n in range(4):
        size = 1 << n
        counts = {"n": n, "functions": 0, "stars": 0, "coordinate_masks": 0}
        for truth in range(1 << size):
            values = [(truth >> x) & 1 for x in range(size)]
            degree = max(
                (
                    support.bit_count()
                    for support in range(size)
                    if sum(
                        (1 - 2 * values[x])
                        * (-1 if (support & x).bit_count() % 2 else 1)
                        for x in range(size)
                    )
                    != 0
                ),
                default=0,
            )
            block_sensitivity = 0
            for centre in range(size):
                sensitive = [
                    block for block in range(1, size)
                    if values[centre ^ block] != values[centre]
                ]

                @lru_cache(None)
                def packing(available):
                    best = ()
                    for block in sensitive:
                        if block & available == block:
                            candidate = (block,) + packing(available ^ block)
                            if len(candidate) > len(best):
                                best = candidate
                    return best

                blocks = packing(size - 1)
                block_sensitivity = max(block_sensitivity, len(blocks))
                leaves = [centre ^ block for block in blocks]
                assert len(leaves) == len(set(leaves)) and centre not in leaves
                matrix = [
                    [
                        int((u == centre and v in leaves) or
                            (v == centre and u in leaves))
                        for v in range(size)
                    ]
                    for u in range(size)
                ]
                # ||Gamma e_centre||^2 equals the number of leaves.
                assert sum(matrix[u][centre] ** 2 for u in range(size)) == len(blocks)
                square_star = [
                    [sum(matrix[u][w] * matrix[w][v] for w in range(size))
                     for v in range(size)]
                    for u in range(size)
                ]
                cube_star = [
                    [sum(square_star[u][w] * matrix[w][v] for w in range(size))
                     for v in range(size)]
                    for u in range(size)
                ]
                assert all(
                    cube_star[u][v] == len(blocks) * matrix[u][v]
                    for u in range(size) for v in range(size)
                )
                for coordinate in range(n):
                    masked = [
                        [
                            matrix[u][v]
                            if ((u >> coordinate) & 1) != ((v >> coordinate) & 1)
                            else 0
                            for v in range(size)
                        ]
                        for u in range(size)
                    ]
                    square = [
                        [
                            sum(masked[w][u] * masked[w][v] for w in range(size))
                            for v in range(size)
                        ]
                        for u in range(size)
                    ]
                    # Exact diagonal projection implies Euclidean norm <= 1.
                    assert all(
                        square[u][v] == 0 if u != v else square[u][v] in (0, 1)
                        for u in range(size)
                        for v in range(size)
                    )
                    counts["coordinate_masks"] += 1
                counts["stars"] += 1

            @lru_cache(None)
            def deterministic_depth(free, fixed):
                remaining_values = {
                    values[fixed | z] for z in range(size) if z & free == z
                }
                if len(remaining_values) == 1:
                    return 0
                return min(
                    1 + max(
                        deterministic_depth(free ^ (1 << i), fixed),
                        deterministic_depth(free ^ (1 << i), fixed | (1 << i)),
                    )
                    for i in range(n) if free >> i & 1
                )

            depth = deterministic_depth(size - 1, 0)
            assert depth <= block_sensitivity * degree
            counts["functions"] += 1
        results.append(counts)

    # Necessary-hypothesis control: OR on two bits has sensitive blocks
    # {0} and {0,1} at 00. These overlap, and coordinate 0 keeps two star edges.
    centre, leaves, size = 0, [1, 3], 4
    overlapping = [
        [int((u == centre and v in leaves) or (v == centre and u in leaves))
         if (u & 1) != (v & 1) else 0
         for v in range(size)]
        for u in range(size)
    ]
    overlapping_centre_norm_sq = sum(overlapping[u][centre] ** 2 for u in range(size))
    assert overlapping_centre_norm_sq == 2

    print(json.dumps({
        "method": "Exhaustive exact-integer tests for all Boolean functions with n <= 3",
        "establishes": [
            "finite degree-zero convention and D <= bs * degree",
            "star centre-vector squared norm equals number of sensitive blocks",
            "exact star identity Gamma^3 = number_of_leaves * Gamma",
            "each masked star squares to a diagonal zero/one projection"
        ],
        "does_not_establish": ["Lean compilation", "the general theorems"],
        "results": results,
        "negative_control": {
            "function": "OR on two input bits",
            "centre": "00",
            "blocks": [[0], [0, 1]],
            "masked_coordinate": 0,
            "centre_unit_vector_output_norm_squared": overlapping_centre_norm_sq,
            "consequence": "Dropping pairwise disjointness invalidates the mask-norm-at-most-one claim"
        }
    }, indent=2))


if __name__ == "__main__":
    main()
