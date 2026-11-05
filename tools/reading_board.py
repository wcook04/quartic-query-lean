"""Construct the three worked experiments from the bound opening of the exposition."""
import re


def board_example(text, scenes):
    lines = text.splitlines()
    a, b = scenes["known-pair"]["selections"][1]["lines"]
    table = []
    for line in lines[a-1:b]:
        if match := re.fullmatch(r"\| Row (\d+) \| ([01] \| [01] \| [01] \| [01]) \|", line):
            if int(match[1]) != len(table) + 1:
                raise ValueError("board example: unexpected row numbering")
            table.append([int(bit) for bit in match[2].split(" | ")])
    if len(table) != 4 or [sum(col) for col in zip(*table)] != [3]*4 or table[3][0] != 0:
        raise ValueError("board example: expected four single-zero columns with the printed change at (4, 1)")
    changed = [row.copy() for row in table]
    changed[3][0] = 1
    scenes["known-pair"].update(original=table, alternative=changed, distinguishing_query={"row": 4, "column": 1},
                                promise="One of these two displayed tables.", query_cost=1)
    scenes["hidden-zeros"].update(
        sampling="Choose one zero row independently and uniformly in each column. In the copy erase one uniformly chosen column’s zero.",
        fixed_row_strategy=[{"rows_read": h, "queries_per_board": 4*h,
                             "difference_seen": {"numerator": h, "denominator": 4}} for h in range(5)],
        yes_certificate="Read every bit of one all-one column.",
        no_certificate="Read a zero in every column.")
    rivals = [2, 3, 4]
    valid = [next(i for i, row in enumerate(changed, 1) if row[j-1] == 0) for j in rivals]
    altered = valid.copy()
    altered[0] = 2
    if valid[0] != 1 or changed[altered[0]-1][1] != 1:
        raise ValueError("board example: altered pointer should now point to one")
    scenes["pointer-check"].update(
        candidate=1, rivals=rivals, correct_pointer_rows=valid, altered_pointer_rows=altered,
        correct_target_bits=[changed[r-1][j-1] for r, j in zip(valid, rivals)],
        altered_target_bits=[changed[r-1][j-1] for r, j in zip(altered, rivals)],
        rival_target_bits=[1, 1, 1],
        comparison="Each rival points into the all-one candidate. Candidate 1 wins when its pointer finds a zero and also wins a tie by its smaller index.",
        conclusion="Changing just this pointer invalidates the certificate while leaving all three comparisons in favour of column 1.")
    return {"paper": "exposition", "coordinates": "one_based_row_and_column",
            "scope": "worked_examples", "scenes": list(scenes.values())}
