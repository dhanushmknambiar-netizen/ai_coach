import random
try:
    from backend.quiz_data import get_quiz_data
except ImportError:
    # Fallback if running from different context
    try:
        from quiz_data import get_quiz_data
    except:
        def get_quiz_data(): return {}

class ResearchTool:
    def __init__(self):
        self.knowledge_base = {
            "Equations and Inequalities": {
                "introduction": "Equations and inequalities are mathematical sentences. An equation says two things are equal (=), while an inequality says one thing is greater or less than another (>, <, ≥, ≤).",
                "deep_dive": [
                    "At their core, equations are about balance. The equals sign (=) acts as a fulcrum; whatever operation you perform on one side, you must perform on the other to maintain this balance. This principle is fundamental to algebra and allows us to isolate variables to find their values.",
                    "Inequalities represent a range of possible solutions rather than a single specific value. For example, x > 5 means x can be any number greater than 5. A crucial rule to remember is that multiplying or dividing by a negative number reverses the direction of the inequality symbol (e.g., -2x < 10 becomes x > -5).",
                    "Understanding these concepts is vital for modeling real-world constraints, such as budget limits (inequalities) or exact resource allocation (equations). systems of equations allow us to solve for multiple unknown variables simultaneously, representing the intersection of conditions."
                ],
                "concepts": [
                    "Linear Equations: ax + b = c",
                    "Inequalities: Solving involves reversing the sign when multiplying by a negative.",
                    "Systems of Equations: Solving for multiple variables simultaneously."
                ],
                "example": {
                    "scenario": "You have a budget of $50 to buy pizza for a party. Each pizza costs $12 and delivery is $5. How many pizzas can you buy?",
                    "steps": [
                        "Define variables: Let x be the number of pizzas.",
                        "Set up inequality: Cost must be less than or equal to budget. 12x + 5 ≤ 50.",
                        "Subtract delivery fee: 12x ≤ 45.",
                        "Divide by cost per pizza: x ≤ 3.75."
                    ],
                    "solution": "Since you can't buy 0.75 of a pizza, x = 3. You can buy exactly 3 pizzas."
                },
                "quiz": [
                    {
                        "question": "What happens to the inequality sign when you divide by a negative number?",
                        "options": ["It stays the same", "It reverses", "It disappears", "It becomes an equal sign"],
                        "correct": 1,
                        "explanation": "Multiplying or dividing an inequality by a negative number changes the direction of the inequality (e.g., > becomes <)."
                    },
                    {
                        "question": "Which of the following is a clear example of a Linear Equation?",
                        "options": ["y = x^2", "y = 2x + 5", "y = 1/x", "y = |x|"],
                        "correct": 1,
                        "explanation": "A linear equation forms a straight line and has no exponents on variables higher than 1. 'y = 2x + 5' is in slope-intercept form."
                    }
                ]
            },
            "Linear Functions": {
                "introduction": "A linear function creates a straight line when graphed. It describes a constant rate of change.",
                 "deep_dive": [
                    "Linear functions describe relationships with a constant rate of change. Visually, they appear as straight lines. The two key characteristics are slope (steepness) and intercept (starting point).",
                    "The slope-intercept form (y = mx + b) is the most common way to represent them. 'm' represents the slope (rise over run), telling you how much y changes for every unit of x. 'b' is the y-intercept, the value of y when x is zero.",
                    "These functions are ubiquitous in modeling simple relationships, such as distance over time at constant speed, or cost over quantity with a fixed unit price."
                ],
                "concepts": [
                    "Slope-Intercept Form: y = mx + b (m is slope, b is y-intercept).",
                    "Rate of Change: How much y changes for every unit of x.",
                    "X and Y Intercepts: Check where the line crosses the axes."
                ],
                "example": {
                    "scenario": "A taxi charges a $3 base fare plus $2 per mile. You travel 10 miles.",
                     "steps": [
                        "Identify variables: m = 2 (rate), b = 3 (start), x = 10 (miles).",
                        "Form equation: y = 2x + 3.",
                        "Substitute x: y = 2(10) + 3.",
                        "Calculate: y = 20 + 3 = 23."
                    ],
                    "solution": "The total cost for the trip is $23."
                }
            },
             "Motion in One Dimension": {
                "introduction": "Motion in one dimension describes objects moving in a straight line, like a car on a highway or a ball dropping.",
                "concepts": [
                    "Displacement: Change in position (vector).",
                    "Velocity: Speed with direction.",
                    "Acceleration: Rate of change of velocity."
                ],
                "example": "A car accelerates from 0 to 60 mph in 5 seconds."
            },
            "Newton's Laws of Motion": {
                "introduction": "Newton's three laws describe the relationship between a body and the forces acting upon it.",
                "concepts": [
                    "1st Law (Inertia): Objects keep doing what they're doing unless forced otherwise.",
                    "2nd Law (F=ma): Force equals mass times acceleration.",
                    "3rd Law: For every action, there is an equal and opposite reaction."
                ],
                "example": "Pushing a shopping cart (F=ma). The heavier the cart, the harder you must push."
            },
            "Python Basics": {
                "introduction": "Python is a high-level, interpreted programming language known for its readability.",
                "concepts": [
                    "Variables: Storing data (x = 5).",
                    "Data Types: Integers, Strings, Floats, Booleans.",
                    "Print Statement: Outputting text to the console."
                ],
                "example": "print('Hello, World!') is the classic first program."
            }
        }
        
        # Load external quiz data
        self.quiz_data = get_quiz_data()

    def search(self, query):
        # fuzzy match or direct lookup
        result_data = None
        for key, data in self.knowledge_base.items():
            if key.lower() in query.lower() or query.lower() in key.lower():
                result_data = data
                break
        
        if not result_data:
             # Fallback procedural generation for unknown topics
            result_data = {
                "introduction": f"The topic '{query}' is a fundamental concept in this subject. It serves as a building block for more advanced theories.",
                "deep_dive": [
                    f"This detailed analysis explores the nuances of {query}. It is essential for understanding the broader context of the subject.",
                    "Researchers and practitioners often rely on these principles to solve complex problems.",
                    "Mastery of {query} requires practice and a solid grasp of the underlying fundamentals."
                ],
                "concepts": [
                    f"Core Principle of {query}",
                    "Applications in real-world scenarios",
                    "Mathematical/Logical representation"
                ],
                "example": {
                    "scenario": f"Imagine applying '{query}' to analyze a daily problem.",
                    "steps": ["Identify the problem.", "Apply the concept.", "Evaluate the result."],
                    "solution": "The problem is solved efficiently."
                }
            }

        # Inject quiz data if available
        # Find matching quiz topic by lowerstring key
        for q_key, q_list in self.quiz_data.items():
             if q_key.lower() in query.lower() or query.lower() in q_key.lower():
                 result_data['quiz'] = q_list
                 break
        
        return result_data
