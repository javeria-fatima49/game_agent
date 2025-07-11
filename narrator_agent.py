class NarratorAgent:
    def __init__(self, model):
        self.model = model

    def narrate(self, user_input: str) -> str:
        prompt = f"""
        You are the game narrator in a fantasy RPG.
        The player said: "{user_input}"

        Narrate what happens next in 2-4 lines. Be descriptive, exciting, and immersive.
        """

        return self.model.generate_content(prompt).text
