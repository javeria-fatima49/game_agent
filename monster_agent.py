from tools.roll_dice import roll_dice

class MonsterAgent:
    def __init__(self, model):
        self.model = model

    def run(self, user_input: str) -> str:
        dice = roll_dice()

        prompt = f"""
        You are a fantasy monster handler in an RPG game.
        The player said: "{user_input}"
        They are engaging in a fight.

        Simulate a battle based on a dice roll result of {dice}.

        If dice >= 4, the player wins. If less, the monster strikes.
        Make it dramatic and short (2-4 lines).
        """

        return self.model.generate_content(prompt).text
