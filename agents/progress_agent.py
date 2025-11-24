import matplotlib.pyplot as plt

class ProgressAgent:
    def __init__(self):
        self.history = {}  

    def update_progress(self, topic, score):
        if topic not in self.history:
            self.history[topic] = []
        self.history[topic].append(score)

    def show_progress(self):
        print("Progress History:")
        for topic, scores in self.history.items():
            print(f"{topic}: {scores}")

    def plot_progress(self):
        for topic, scores in self.history.items():
            plt.plot(range(1, len(scores)+1), scores, marker='o', label=topic)
        plt.title("Progress Over Time")
        plt.xlabel("Session")
        plt.ylabel("Score (%)")
        plt.ylim(0, 100)
        plt.legend()
        plt.show()
