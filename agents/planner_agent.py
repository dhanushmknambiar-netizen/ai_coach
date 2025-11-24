class PlannerAgent:
    def __init__(self):
       self.session_plan = []
       self.current_index = 0

    def create_plan(self, topics):
        self.session_plan = topics  
        self.current_index = 0
        return self.session_plan

    def show_plan(self):
        print("Today's Study Plan:")
        for idx, topic in enumerate(self.session_plan, 1):
            print(f"{idx}. {topic}")

    def get_next_topic(self):
        if self.current_index < len(self.session_plan):
            topic = self.session_plan[self.current_index]
            self.current_index += 1
            return topic
        return None

    def pause(self):
        return {"session_plan": self.session_plan, "current_index": self.current_index}
    
    def resume(self, state):
        if not state:
            return
        self.session_plan = state.get("session_plan", [])
        self.current_index = state.get("current_index", 0)