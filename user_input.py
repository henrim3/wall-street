def choice_input(options: list[str], prompt: str, title: str = None) -> int:
    """ Get user input for a choice from multiple options

        Args:
            options (list[str]): Options the user can choose from.
            prompt (str): Prompt given to the user.
            title (str, optional): Title of the prompt. Defaults to None.

        Returns:
            Tuple[int, str]: Index and value of the option chosen.
    """
    output: str = "\n"

    if title is not None:
        output += title
        if not title.endswith("\n"):
            output += "\n"

    i: int
    option: str
    for i, option in enumerate(options):
        output += f"{i + 1}: {option}\n"

    print(output)

    input_num: int
    while True:
        user_input: str = input(prompt)

        # try to convert input to int
        try:
            input_num = int(user_input)
            if input_num >= 1 and input_num <= len(options):
                break
            else:
                print(f"Error: Input must be between 1 and {len(options)}")
        except ValueError:
            print("Error: Input must be a number.")

        print()

    # 0-indexed
    return (input_num - 1, options[input_num - 1])
