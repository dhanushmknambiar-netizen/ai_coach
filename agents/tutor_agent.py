# agents/tutor_agent.py

from tools.tools import ResearchTool

class TutorAgent:
    def __init__(self):
        # Research tool simulates web lookup / knowledge fetch
        self.research = ResearchTool()
        self.current_topic = None

    def teach(self, plan):
        """Old helper: produce a combined content string for the full plan (kept for compatibility)."""
        content = "Here is your personalized study content:\n\n"
        for item in plan:
            content += f"- {item}: Explanation + example + mini quiz\n"
        return content

    def teach_topic(self, topic):
        """Teach a single topic (used in the session loop)."""
        self.current_topic = topic
        # Use research tool to fetch an explanation snippet
        snippet = self.research.search(topic)
        explanation = f"Explanation of {topic}: {snippet}"
        print(explanation)
        return explanation

    def generate_quiz(self):
        """
        Generate a simple quiz for the current topic.
        Returns a list of question strings.
        """
        if not self.current_topic:
            print("No topic selected for quiz generation.")
            return []

        # very simple question set — can be improved later
        quiz = [
            f"What is the main idea of {self.current_topic}?",
            f"Give one short example of {self.current_topic}.",
            f"Solve a small practice related to {self.current_topic}."
        ]
        return quiz
