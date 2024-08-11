from turn import Turn


def run_turns(turns: list[list[Turn, int]]):
    turn_number: int = 1
    for t in turns:
        turn: Turn = t[0]
        n: int = t[1]
        for i in range(turn_number, turn_number + n):
            turn.run(i)
        turn_number += n
