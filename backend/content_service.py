"""
Content Module inspired by OpenStax structure.
Provides subjects and topics.
"""

# Mock Data simulating a database or OpenStax API
OPENSTAX_DATA = {
    "math": [
        {"id": "alg-1", "title": "College Algebra", "topics": ["Equations and Inequalities", "Functions", "Linear Functions", "Polynomial and Rational Functions"]},
        {"id": "calc-1", "title": "Calculus Vol 1", "topics": ["Limits", "Derivatives", "Applications of Derivatives", "Integration"]}
    ],
    "physics": [
        {"id": "phy-1", "title": "University Physics Vol 1", "topics": ["Units and Measurement", "Vectors", "Motion Along a Straight Line", "Newton's Laws of Motion"]},
        {"id": "phy-2", "title": "University Physics Vol 2", "topics": ["Thermodynamics", "Electricity and Magnetism", "Optics"]}
    ],
    "python": [
        {"id": "py-1", "title": "Introduction to Python", "topics": ["Variables", "Loops", "Functions", "Classes"]}
    ]
}

def get_subjects():
    return list(OPENSTAX_DATA.keys())

def get_topics_by_subject(subject_key):
    return OPENSTAX_DATA.get(subject_key.lower(), [])
