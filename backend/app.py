from flask import Flask, jsonify, render_template
from flask_cors import CORS
import content_service
import os
import sys

base_dir = os.path.abspath(os.path.dirname(__file__))
# Add parent dir to path to allow importing agents
sys.path.append(os.path.join(base_dir, '..'))

app = Flask(__name__, 
            static_folder=os.path.join(base_dir, 'static'), 
            template_folder=os.path.join(base_dir, 'templates'))
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/subjects', methods=['GET'])
def get_subjects():
    return jsonify(content_service.get_subjects())

@app.route('/api/topics/<subject>', methods=['GET'])
def get_topics(subject):
    topics = content_service.get_topics_by_subject(subject)
    if not topics:
        return jsonify({"error": "Subject not found"}), 404
    return jsonify(topics)

# Initialize Agents
try:
    from agents.tutor_agent import TutorAgent
    tutor = TutorAgent()
except ImportError:
    # Fallback/Mock if agents not found (for robustness)
    class MockTutor:
        def teach_topic(self, t): return f"Mock explanation for {t}"
        def generate_quiz(self): return ["Q1?", "Q2?"]
    tutor = MockTutor()

@app.route('/api/teach', methods=['POST'])
def teach_topic():
    from flask import request
    data = request.json
    topic = data.get('topic')
    if not topic:
        return jsonify({"error": "No topic provided"}), 400
    
    
    # result contains both explanation HTML and structured quiz data
    result = tutor.teach_topic(topic)
    
    # Check if result is dict (new agent) or string (mock/old agent)
    if isinstance(result, dict):
        explanation = result.get('explanation', '')
        quiz = result.get('quiz', [])
    else:
        explanation = result
        quiz = tutor.generate_quiz() # Fallback
    
    return jsonify({
        "topic": topic,
        "explanation": explanation,
        "quiz": quiz
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
