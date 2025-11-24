class SummarizerAgent:
    def __init__(self):
        self.summaries = []

    def create_summary(self, progress_history):
        summary_text = "Study Summary:\n"
        for topic, scores in progress_history.items():
            avg_score = sum(scores)/len(scores)
            summary_text += f"{topic}: Average Score = {avg_score:.1f}%\n"
        self.summaries.append(summary_text)
        return summary_text

    def show_summary(self):
        for summary in self.summaries:
            print(summary)
