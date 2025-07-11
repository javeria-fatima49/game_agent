from tools.generate_event import generate_event

class ItemAgent:
    def __init__(self, model):
        self.model = model

    def reward(self, user_input: str) -> str:
        event = generate_event()

        prompt = f"""
        You are a fantasy item master. The player did: "{user_input}"
        They found: {event}

        Respond with a magical, short reward message (2–3 lines) based on the event.
        Make it immersive and fun.
        """

        return self.model.generate_content(prompt).text
