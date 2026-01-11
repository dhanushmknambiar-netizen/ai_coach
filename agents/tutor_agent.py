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
        # Use research tool to fetch structured content
        data = self.research.search(topic)
        
        deep_dive_html = "".join([f"<p style='margin-bottom: 0.8rem;'>{p}</p>" for p in data.get('deep_dive', [])])
        
        example_data = data['example']
        if isinstance(example_data, dict):
            steps_html = "".join([f"<li style='margin-bottom: 0.5rem;'>{s}</li>" for s in example_data['steps']])
            example_html = f"""
                <p><strong>Scenario:</strong> {example_data['scenario']}</p>
                <ol style="margin-left: 20px; margin-top: 10px; color: #ccc;">{steps_html}</ol>
                <p style="margin-top: 10px; color: #a0a0ff;"><strong>Solution:</strong> {example_data['solution']}</p>
            """
        else:
            example_html = f"<p>{example_data}</p>"


        # Format into HTML for the frontend
        html_content = f"""
        <div class="lesson-content">
            <h3 style="color: #fff; margin-bottom: 0.5rem;">Introduction</h3>
            <p class="intro" style="font-size: 1.1rem; margin-bottom: 1.5rem;">{data['introduction']}</p>
            
            <h4 style="color: #a0a0ff; margin-bottom: 0.5rem;">Deep Dive Analysis</h4>
            <div style="line-height: 1.6; color: #ddd; margin-bottom: 1.5rem;">
                {deep_dive_html}
            </div>
            
            <h4 style="color: #a0a0ff; margin-bottom: 0.5rem;">Key Concepts</h4>
            <ul style="margin-left: 20px; list-style-type: disc; margin-bottom: 1.5rem;">
                {''.join([f'<li style="margin-bottom: 0.5rem;">{c}</li>' for c in data['concepts']])}
            </ul>
            
            <h4 style="color: #a0a0ff; margin-bottom: 0.5rem;">Real World Example</h4>
            <div class="example-box" style="background: rgba(255,255,255,0.05); padding: 15px; border-left: 3px solid #6c5ce7; border-radius: 8px;">
                {example_html}
            </div>
        </div>
        """
        
        # Return structured data. Note: Fallback procedural generation in tools.py might not have 'quiz' key yet, 
        # so we should handle that safe-guard, but properly tools.py should be updated.
        # For now, let's assume tools.py has it or we default to empty.
        quiz_data = data.get('quiz', [])
        
        return {
            "explanation": html_content,
            "quiz": quiz_data
        }

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
