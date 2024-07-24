class Turn():
    def __init__(self) -> None:
        self.name: str
        self.turn_number: int

    def run(self) -> None:
        raise NotImplementedError()

    def output(self) -> None:
        print(f"---- {self.name}: Turn {self.turn_number} ----")
