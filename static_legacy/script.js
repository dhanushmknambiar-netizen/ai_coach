const api = {
    start: async () => {
        const res = await fetch('/api/start', { 
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ topics: ["Math", "Physics", "Python"] })
        });
        return res.json();
    },
    teach: async (topic) => {
        const res = await fetch('/api/teach', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ topic })
        });
        return res.json();
    },
    quiz: async () => {
        const res = await fetch('/api/quiz', { method: 'POST' });
        return res.json();
    },
    evaluate: async (answers) => {
        const res = await fetch('/api/evaluate', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ answers })
        });
        return res.json();
    },
    progress: async () => {
        const res = await fetch('/api/progress');
        return res.json();
    }
};

let currentPlan = [];
let currentTopic = null;
let chartInstance = null;

function showSection(id) {
    document.querySelectorAll('section').forEach(s => {
        s.classList.remove('active-section');
        s.classList.add('hidden-section');
    });
    
    document.getElementById(`${id}-section`).classList.remove('hidden-section');
    document.getElementById(`${id}-section`).classList.add('active-section');

    document.querySelectorAll('.nav-links li').forEach(l => l.classList.remove('active'));
    // Find the nav link that called this (approximate)
    if(id === 'home') document.querySelector('.nav-links li:nth-child(1)').classList.add('active');
    if(id === 'plan') document.querySelector('.nav-links li:nth-child(2)').classList.add('active');
    if(id === 'progress') {
        document.querySelector('.nav-links li:nth-child(3)').classList.add('active');
        loadProgress();
    }
}

async function startSession() {
    const data = await api.start();
    currentPlan = data.plan;
    renderPlan();
    showSection('plan');
    document.getElementById('status-text').innerText = "In Progress";
}

function renderPlan() {
    const container = document.getElementById('plan-list');
    container.innerHTML = '';
    currentPlan.forEach((topic, idx) => {
        const card = document.createElement('div');
        card.className = `topic-card ${idx === 0 ? 'active' : ''}`; // Default first active
        card.onclick = () => selectTopic(topic, card);
        card.innerHTML = `
            <h4>${topic}</h4>
            <div class="topic-status">Pending</div>
        `;
        container.appendChild(card);
    });
    if(currentPlan.length > 0) {
        selectTopic(currentPlan[0], container.children[0]);
    }
}

function selectTopic(topic, cardElem) {
    currentTopic = topic;
    document.querySelectorAll('.topic-card').forEach(c => c.classList.remove('active'));
    if(cardElem) cardElem.classList.add('active');
    
    document.getElementById('learning-area').classList.remove('hidden');
    document.getElementById('current-topic-title').innerText = topic;
    document.getElementById('explanation-content').innerHTML = '<p class="placeholder-text">Click "Explain This" to start learning.</p>';
    document.getElementById('quiz-area').classList.add('hidden');
}

async function teachCurrentTopic() {
    if(!currentTopic) return;
    document.getElementById('explanation-content').innerHTML = '<p>Loading explanation...</p>';
    const data = await api.teach(currentTopic);
    
    // Animate text roughly
    document.getElementById('explanation-content').innerHTML = `<p>${data.explanation}</p>`;
}

async function startQuiz() {
    document.getElementById('quiz-area').classList.remove('hidden');
    const container = document.getElementById('quiz-questions');
    container.innerHTML = '<p>Generating quiz...</p>';
    
    const data = await api.quiz();
    container.innerHTML = '';
    
    if(data.questions) {
        data.questions.forEach((q, idx) => {
            const div = document.createElement('div');
            div.className = 'quiz-question';
            div.innerHTML = `
                <p><strong>Q${idx+1}:</strong> ${q}</p>
                <input type="text" class="quiz-input" data-idx="${idx}" placeholder="Your answer...">
            `;
            container.appendChild(div);
        });
    }
}

async function submitQuiz() {
    const inputs = document.querySelectorAll('.quiz-input');
    const answers = [];
    inputs.forEach(inp => answers.push(inp.value));
    
    const res = await api.evaluate(answers);
    
    alert(`Score: ${res.score}%\nCorrect: ${res.correct_count}/${res.total_questions}`);
    
    // Determine status update
    // Simple visual update
    updateOverallProgress();
}

function updateOverallProgress() {
    // Just a dummy increment for demo
    const bar = document.getElementById('overall-progress');
    let w = parseInt(bar.style.width || 0);
    w = Math.min(w + 33, 100);
    bar.style.width = `${w}%`;
}

async function loadProgress() {
    const data = await api.progress();
    const ctx = document.getElementById('progressChart').getContext('2d');
    
    const labels = Object.keys(data);
    
    // Flatten scores to get average per topic for chart
    const avgScores = labels.map(topic => {
        const scores = data[topic];
        const sum = scores.reduce((a, b) => a + b, 0);
        return (sum / scores.length) || 0;
    });

    if(chartInstance) chartInstance.destroy();

    chartInstance = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Average Score (%)',
                data: avgScores,
                backgroundColor: 'rgba(108, 99, 255, 0.6)',
                borderColor: 'rgba(108, 99, 255, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100,
                    grid: { color: 'rgba(255, 255, 255, 0.1)' },
                    ticks: { color: '#a0a0b0' }
                },
                x: {
                    grid: { display: false },
                    ticks: { color: '#a0a0b0' }
                }
            },
            plugins: {
                legend: { labels: { color: '#fff' } }
            }
        }
    });

    const stats = document.getElementById('stats-content');
    if(labels.length === 0) {
        stats.innerHTML = "<p>No sessions completed yet.</p>";
    } else {
        stats.innerHTML = labels.map(l => `<p><strong>${l}:</strong> ${data[l].length} quiz(zes) taken.</p>`).join('');
    }
}
