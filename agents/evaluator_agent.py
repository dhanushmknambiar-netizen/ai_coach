# agents/evaluator_agent.py

class EvaluatorAgent:
    def __init__(self):
        self.results = {}  # topic -> score list

    def generate_quiz(self, content):
        """
        Creates a simple list-of-questions quiz from the study content.
        """
        # A very simple quiz generator; adjust later to use content parsing
        quiz = [
            "Question 1: Define the key concept.",
            "Question 2: Give one example.",
            "Question 3: Solve a short practice problem."
        ]
        return quiz

    def evaluate(self, quiz, answers):
        """
        Evaluate the answers (quiz: list, answers: list).
        Simple simulated grading: treat even-indexed answers as correct.
        Returns percentage score (0-100).
        """
        if not quiz:
            return 0.0

        correct = 0
        for i in range(len(quiz)):
            # If an answer exists for this question, simulate correctness:
            if i < len(answers):
                # simple simulation: treat even-indexed answers as correct
                if i % 2 == 0:
                    correct += 1
            # if no answer provided, treat as incorrect

        pct = (correct / len(quiz)) * 100
        return pct

    def evaluate_quiz(self, topic, quiz, answers):
        """
        Wrapper used by main.py.
        Calls existing evaluate() and stores the score.
        """
        score = self.evaluate(quiz, answers)

        # store per-topic results (list of scores)
        if topic not in self.results:
            self.results[topic] = []
        self.results[topic].append(score)

        return score
