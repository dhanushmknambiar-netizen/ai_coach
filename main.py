from agents.session_manager import SessionManager
from memory.memory import Memory
from agents.planner_agent import PlannerAgent
from agents.tutor_agent import TutorAgent
from agents.evaluator_agent import EvaluatorAgent
from agents.progress_agent import ProgressAgent
from agents.summarizer_agent import SummarizerAgent


memory = Memory()
session_mgr = SessionManager(memory)
planner = PlannerAgent()
tutor = TutorAgent()
evaluator = EvaluatorAgent()
progress_tracker = ProgressAgent()
summarizer = SummarizerAgent()


topics = ["Math", "Physics", "Python"]
plan = planner.create_plan(topics)
planner.show_plan()
content = tutor.teach(plan)
quiz = evaluator.generate_quiz(content)
score = evaluator.evaluate(quiz, ["A", "B", "C"])
summary = summarizer.create_summary(progress_tracker.history)
summarizer.show_summary()
session_mgr.save_session(summary)


start_idx = session_mgr.load_index()
if start_idx and start_idx > 0:
    print(f"Resuming from topic index {start_idx} (0-based).")

for i in range(start_idx, len(plan)):
    topic = plan[i]
    print(f"\n--- Session for topic {i} : {topic} ---")
    tutor.teach_topic(topic)
    quiz = tutor.generate_quiz()
    print("Generated Quiz:")
    for q in quiz:
        print(q)

    
    answers = ["Answer 1", "Answer 2"]
    score = evaluator.evaluate_quiz(topic, quiz, answers)
    progress_tracker.update_progress(topic, score)


    
    while True:
        choice = input("Enter (C)ontinue, (P)ause and save, or (Q)uit without saving: ").strip().lower()
        if choice == "c" or choice == "continue":
            
            session_mgr.save_index(i + 1)  
            break
        elif choice == "p" or choice == "pause":
            
            session_mgr.save_index(i + 1)
            print(f"Session paused. You can resume later from topic index {i+1}.")
            exit(0)
        elif choice == "q" or choice == "quit":
            
            print("Exiting without saving resume index.")
            exit(0)
        else:
            print("Please enter C, P, or Q.")


session_mgr.clear()
print("\nAll topics completed for this session.")
