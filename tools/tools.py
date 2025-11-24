import random

class ResearchTool:
    def search(self, query):
        sample_results = [
            "This topic is important because it improves problem-solving.",
            "Students usually struggle with this area.",
            "Recommended study duration is 30 minutes.",
            "Best method: active recall + spaced repetition."
        ]
        return random.choice(sample_results)
