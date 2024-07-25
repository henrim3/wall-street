class Action:
    def __init__(self) -> None:
        self.name: str
        self.end_turn: bool = False
        self.one_time: bool = False

    def __init_subclass__(self):
        Action.__init__(self)

    def run(self) -> None:
        raise NotImplementedError()
