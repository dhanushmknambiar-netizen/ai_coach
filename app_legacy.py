import os
import json
from flask import Flask, render_template, jsonify, request
from agents.planner_agent import PlannerAgent
from agents.tutor_agent import TutorAgent
from agents.evaluator_agent import EvaluatorAgent
from agents.progress_agent import ProgressAgent
from agents.session_manager import SessionManager
from memory.memory import Memory

app = Flask(__name__)

# Initialize Agents
memory = Memory()
session_mgr = SessionManager(memory)
planner = PlannerAgent()
tutor = TutorAgent()
evaluator = EvaluatorAgent()
progress_tracker = ProgressAgent()

# Global state for simple session management in memory (for demo purposes)
# In a real app, this would be in a database or session cookie
current_session_state = {
    "plan": [],
    "current_topic_index": 0,
    "current_quiz": [],
    "current_topic": None
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/start', methods=['POST'])
def start_session():
    data = request.json
    topics = data.get('topics', ["Math", "Physics", "Python"])
    
    plan = planner.create_plan(topics)
    current_session_state["plan"] = plan
    current_session_state["current_topic_index"] = 0
    current_session_state["current_topic"] = None
    current_session_state["current_quiz"] = []
    
    return jsonify({
        "message": "Session started",
        "plan": plan
    })

@app.route('/api/get_plan', methods=['GET'])
def get_plan():
    return jsonify({
        "plan": current_session_state["plan"],
        "current_index": current_session_state["current_topic_index"]
    })

@app.route('/api/teach', methods=['POST'])
def teach_topic():
    data = request.json
    topic = data.get('topic')
    
    # If no topic provided, use current from plan
    if not topic:
        idx = current_session_state["current_topic_index"]
        plan = current_session_state["plan"]
        if idx < len(plan):
            topic = plan[idx]
        else:
            return jsonify({"error": "No more topics in plan", "finished": True}), 400

    current_session_state["current_topic"] = topic
    
    # Use Tutor Agent
    explanation = tutor.teach_topic(topic)
    
    return jsonify({
        "topic": topic,
        "explanation": explanation
    })

@app.route('/api/quiz', methods=['POST'])
def generate_quiz():
    topic = current_session_state.get("current_topic")
    if not topic:
         return jsonify({"error": "No active topic to quiz"}), 400
         
    # Generate quiz
    # Tutor agent generates quiz questions
    questions = tutor.generate_quiz()
    current_session_state["current_quiz"] = questions
    
    return jsonify({
        "topic": topic,
        "questions": questions
    })

@app.route('/api/evaluate', methods=['POST'])
def evaluate_quiz():
    data = request.json
    answers = data.get('answers', []) # List of strings
    topic = current_session_state.get("current_topic")
    
    quiz_questions = current_session_state.get("current_quiz", [])
    
    if not quiz_questions:
        return jsonify({"error": "No active quiz"}), 400
        
    # Evaluate
    score = evaluator.evaluate_quiz(topic, quiz_questions, answers)
    
    # Update progress
    progress_tracker.update_progress(topic, score)
    
    # Advance topic index
    current_session_state["current_topic_index"] += 1
    
    return jsonify({
        "score": score,
        "topic": topic,
        "total_questions": len(quiz_questions),
        "correct_count": int((score / 100) * len(quiz_questions))
    })

@app.route('/api/progress', methods=['GET'])
def get_progress():
    return jsonify(progress_tracker.history)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
