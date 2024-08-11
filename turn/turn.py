class Turn():
    def __init__(self) -> None:
        self.name: str

    def run(self, turn_number: int) -> None:
        raise NotImplementedError()

    def output(self, turn_number: int) -> None:
        print(f"---- {self.name}: Turn {turn_number} ----")
