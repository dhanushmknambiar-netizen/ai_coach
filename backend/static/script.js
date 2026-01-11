const api = {
    getSubjects: async () => {
        const res = await fetch('/api/subjects');
        return res.json();
    },
    getTopics: async (subject) => {
        const res = await fetch(`/api/topics/${subject}`);
        return res.json();
    },
    teach: async (topic) => {
        const res = await fetch('/api/teach', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ topic })
        });
        return res.json();
    }
};

function showSection(id) {
    document.querySelectorAll('section').forEach(s => {
        s.classList.remove('active-section');
        s.classList.add('hidden-section');
        s.style.display = ''; // Clear inline styles that might override classes
    });

    document.getElementById(`${id}-section`).classList.remove('hidden-section');
    document.getElementById(`${id}-section`).classList.add('active-section');

    document.querySelectorAll('.nav-links li').forEach(l => l.classList.remove('active'));
    if (id === 'home') document.querySelector('.nav-links li:nth-child(1)').classList.add('active');
    if (id === 'subjects' || id === 'topics') document.querySelector('.nav-links li:nth-child(2)').classList.add('active');
    if (id === 'progress') document.querySelector('.nav-links li:nth-child(3)').classList.add('active');

    if (id === 'home' && typeof loadRecentTopics === 'function') {
        loadRecentTopics();
    }
}

// Load and render recent topics list
function loadRecentTopics() {
    let recentTopics = [];
    try {
        recentTopics = JSON.parse(localStorage.getItem('recentTopics') || '[]');
    } catch (e) {
        recentTopics = [];
    }

    const wrapper = document.getElementById('recent-topics-wrapper');
    const list = document.getElementById('recent-list');

    if (recentTopics.length > 0) {
        list.innerHTML = '';
        recentTopics.forEach(topic => {
            const item = document.createElement('div');
            item.className = 'glass-card';
            item.style.padding = '10px 15px';
            item.style.cursor = 'pointer';
            item.style.display = 'flex';
            item.style.justifyContent = 'space-between';
            item.style.alignItems = 'center';
            item.style.background = 'rgba(255, 255, 255, 0.05)';

            item.innerHTML = `
                <span style="color: #fff; font-weight: 500;">${topic}</span>
                <span style="color: var(--primary-color);font-size: 0.9rem;">Continue &rarr;</span>
            `;
            item.onclick = () => startLearning(topic);
            list.appendChild(item);
        });
        wrapper.style.display = 'block';
    } else {
        wrapper.style.display = 'none';
    }
}

// Initialize on load
document.addEventListener('DOMContentLoaded', () => {
    loadRecentTopics();
    // Default show home
    showSection('home');
});

async function loadSubjects() {

    // Already static in HTML for now, but could be dynamic
    // const subjects = await api.getSubjects();
    showSection('subjects');
}

async function loadTopicsForSubject(subject) {
    document.getElementById('selected-subject-title').innerText = subject.charAt(0).toUpperCase() + subject.slice(1) + " Topics";

    const container = document.getElementById('topic-list-container');
    container.innerHTML = '<p>Loading topics...</p>';
    showSection('topics');

    try {
        const units = await api.getTopics(subject);
        container.innerHTML = '';

        if (units.length === 0) {
            container.innerHTML = '<p>No topics found.</p>';
            return;
        }

        units.forEach(unit => {
            const card = document.createElement('div');
            card.className = 'glass-card full-width'; // Use card style

            let topicsHtml = '<ul style="margin-top: 10px; margin-left: 20px;">';
            unit.topics.forEach(t => {
                topicsHtml += `<li style="margin-bottom: 5px; color: #ccc;">${t}</li>`;
            });
            topicsHtml += '</ul>';

            card.innerHTML = `
                <h3 style="color: #a0a0ff;">${unit.title}</h3>
                ${topicsHtml}
            `;

            // Add click handlers to list items
            const listItems = card.querySelectorAll('li');
            listItems.forEach(li => {
                li.style.cursor = 'pointer';
                li.style.textDecoration = 'underline';
                li.onclick = () => startLearning(li.innerText);
            });

            container.appendChild(card);
        });
    } catch (e) {
        console.error(e);
        container.innerHTML = '<p>Error loading topics.</p>';
    }
}

// Global variable to store current quiz data
let currentQuizData = [];

async function startLearning(topic) {
    // Hide all sections
    document.querySelectorAll('section').forEach(el => {
        el.classList.remove('active-section');
        el.classList.add('hidden-section');
        // fallback if styles were set directly
        el.style.display = '';
    });

    // Show learning section
    const learningSec = document.getElementById('learning-section');
    learningSec.classList.remove('hidden-section');
    learningSec.classList.add('active-section');
    learningSec.style.display = 'block';

    // Reset state
    document.getElementById('learning-topic-title').innerText = topic;
    document.getElementById('learning-content').innerHTML = '<div class="loading-spinner"></div>';
    document.getElementById('quiz-container').innerHTML = ''; // Clear previous quiz
    currentQuizData = []; // Clear data

    // Save as recent (manage array of 3)
    let recentTopics = [];
    try {
        recentTopics = JSON.parse(localStorage.getItem('recentTopics') || '[]');
    } catch (e) {
        recentTopics = [];
    }

    // Remove if exists (to move to top)
    recentTopics = recentTopics.filter(t => t !== topic);

    // Add to top
    recentTopics.unshift(topic);

    // Keep max 3
    if (recentTopics.length > 3) {
        recentTopics = recentTopics.slice(0, 3);
    }

    localStorage.setItem('recentTopics', JSON.stringify(recentTopics));

    try {
        const data = await api.teach(topic);
        document.getElementById('learning-content').innerHTML = data.explanation;

        // Store quiz data for later use
        currentQuizData = data.quiz || [];

        // Show Take Quiz Button
        document.getElementById('take-quiz-btn-container').innerHTML = `
            <button class="btn-primary" onclick="showQuiz()">Take Quiz</button>
        `;

    } catch (e) {
        document.getElementById('learning-content').innerText = "Error generating content.";
        console.error(e);
    }
}

function showQuiz() {
    // Hide all sections
    document.querySelectorAll('section').forEach(el => {
        el.classList.remove('active-section');
        el.classList.add('hidden-section');
        el.style.display = '';
    });

    // Show quiz section
    const quizSec = document.getElementById('quiz-section');
    quizSec.classList.remove('hidden-section');
    quizSec.classList.add('active-section');
    quizSec.style.display = 'block';

    renderQuiz();
}

function backToLesson() {
    // Hide all sections
    document.querySelectorAll('section').forEach(el => {
        el.classList.remove('active-section');
        el.classList.add('hidden-section');
        el.style.display = '';
    });

    // Show learning section
    const learningSec = document.getElementById('learning-section');
    learningSec.classList.remove('hidden-section');
    learningSec.classList.add('active-section');
    learningSec.style.display = 'block';
}

function renderQuiz() {
    const quizContainer = document.getElementById('quiz-container');
    quizContainer.innerHTML = ''; // Ensure clear

    if (currentQuizData && currentQuizData.length > 0) {
        currentQuizData.forEach((q, index) => {
            // Interactive MCQ
            const questionId = `q${index}`;
            let optionsHtml = '';
            q.options.forEach((opt, optIndex) => {
                optionsHtml += `
                    <div style="margin-bottom: 5px;">
                        <input type="radio" name="${questionId}" id="${questionId}_opt${optIndex}" value="${optIndex}">
                        <label for="${questionId}_opt${optIndex}" style="cursor: pointer; color: #ccc;">${opt}</label>
                    </div>
                `;
            });

            const questionHtml = `
                <div class="quiz-card" style="background: rgba(255, 255, 255, 0.05); padding: 15px; border-radius: 8px; margin-bottom: 15px;">
                    <p style="font-weight: bold; color: #fff; margin-bottom: 10px;">Q${index + 1}: ${q.question}</p>
                    <form id="form_${questionId}">
                        ${optionsHtml}
                    </form>
                    <button onclick="checkAnswer(${index}, ${q.correct})" style="margin-top: 10px; padding: 5px 15px; background: #6c5ce7; border: none; border-radius: 4px; color: white; cursor: pointer; font-size: 0.9rem;">Check Answer</button>
                    <div id="feedback_${index}" style="margin-top: 10px; font-weight: bold; display: none;"></div>
                    <div id="explanation_${index}" style="margin-top: 5px; color: #aaa; font-size: 0.9rem; display: none;">${q.explanation}</div>
                </div>
            `;
            quizContainer.innerHTML += questionHtml;
        });
    } else {
        quizContainer.innerHTML = '<p>No quiz available for this topic.</p>';
    }
}

function checkAnswer(questionIndex, correctIndex) {
    const questionId = `q${questionIndex}`;
    const selected = document.querySelector(`input[name="${questionId}"]:checked`);
    const feedbackEl = document.getElementById(`feedback_${questionIndex}`);
    const explanationEl = document.getElementById(`explanation_${questionIndex}`);

    if (!selected) {
        feedbackEl.style.display = 'block';
        feedbackEl.style.color = '#ff7675';
        feedbackEl.innerText = "Please select an answer.";
        return;
    }

    const selectedValue = parseInt(selected.value);

    if (selectedValue === correctIndex) {
        feedbackEl.style.display = 'block';
        feedbackEl.style.color = '#55efc4'; // Green
        feedbackEl.innerText = "Correct! ✅";
        explanationEl.style.display = 'block';
    } else {
        feedbackEl.style.display = 'block';
        feedbackEl.style.color = '#ff7675'; // Red
        feedbackEl.innerText = "Incorrect. Try again!";
        explanationEl.style.display = 'none';
    }
}
