# This file contains the quiz data for all topics
# Each topic has a list of 10 questions

def get_quiz_data():
    return {
        # --- MATH ---
        "Equations and Inequalities": [
            {"question": "What is the solution to 2x = 10?", "options": ["x=2", "x=5", "x=10", "x=0"], "correct": 1, "explanation": "Divide both sides by 2."},
            {"question": "Solve for x: x - 5 > 10.", "options": ["x > 5", "x > 15", "x < 15", "x = 15"], "correct": 1, "explanation": "Add 5 to both sides."},
            {"question": "What does a filled circle on a number line represent?", "options": ["Strict inequality (< or >)", "Inclusive inequality (≤ or ≥)", "Equal to", "Undefined"], "correct": 1, "explanation": "A filled circle includes the number."},
            {"question": "If -3x < 9, then...", "options": ["x < -3", "x > -3", "x < 3", "x > 3"], "correct": 1, "explanation": "Dividing by a negative number reverses the sign."},
            {"question": "Which is a linear equation?", "options": ["y = x^2", "y = 1/x", "y = 3x + 1", "y = sqrt(x)"], "correct": 2, "explanation": "No exponents or roots on variables."},
            {"question": "Solve: 2(x+1) = 4.", "options": ["1", "2", "3", "0"], "correct": 0, "explanation": "2x+2=4 -> 2x=2 -> x=1."},
            {"question": "What is the inverse operation of addition?", "options": ["Multiplication", "Division", "Subtraction", "Squaring"], "correct": 2, "explanation": "Subtraction undoes addition."},
            {"question": "Is 5 a solution to 2x > 10?", "options": ["Yes", "No", "Maybe", "Depends"], "correct": 1, "explanation": "2(5) = 10, which is not strictly greater than 10."},
            {"question": "System: x+y=2, x-y=0. What is x?", "options": ["0", "1", "2", "3"], "correct": 1, "explanation": "Add equations: 2x=2 -> x=1."},
            {"question": "Absolute value |x| = 3 implies...", "options": ["x=3", "x=-3", "x=3 or x=-3", "x=9"], "correct": 2, "explanation": "Distance from zero is 3 in both directions."}
        ],
        "Linear Functions": [
             {"question": "Which form is Slope-Intercept?", "options": ["Ax+By=C", "y=mx+b", "y-y1=m(x-x1)", "y=a(x-h)^2+k"], "correct": 1, "explanation": "y=mx+b is slope-intercept form."},
             {"question": "What is 'm' in y=mx+b?", "options": ["y-intercept", "slope", "x-intercept", "midpoint"], "correct": 1, "explanation": "m represents the slope (rise/run)."},
             {"question": "What is 'b' in y=mx+b?", "options": ["slope", "y-intercept", "x-intercept", "origin"], "correct": 1, "explanation": "b is where the line crosses the y-axis."},
             {"question": "Find the slope of y = 3x - 2.", "options": ["3", "-2", "2", "x"], "correct": 0, "explanation": "Coefficient of x is the slope."},
             {"question": "Find the y-intercept of y = -x + 5.", "options": ["-1", "0", "1", "5"], "correct": 3, "explanation": "Constant term is the y-intercept."},
             {"question": "Slope of a horizontal line is...", "options": ["Undefined", "1", "0", "Infinite"], "correct": 2, "explanation": "There is no rise, so rise/run = 0."},
             {"question": "Slope of a vertical line is...", "options": ["Undefined", "1", "0", "Negative"], "correct": 0, "explanation": "Run is 0, division by zero is undefined."},
             {"question": "Equation of line with slope 2 passing through (0,0).", "options": ["y=2x", "y=x+2", "y=2", "x=2"], "correct": 0, "explanation": "y = mx + b -> y = 2x + 0."},
             {"question": "What does a positive slope indicate?", "options": ["Line goes down", "Line goes up", "Line is flat", "Line is vertical"], "correct": 1, "explanation": "As x increases, y increases."},
             {"question": "Are parallel lines' slopes equal?", "options": ["Yes", "No", "Sometimes", "Only if vertical"], "correct": 0, "explanation": "Parallel lines never touch, so they have the same steepness."}
        ],
        "Functions": [
            {"question": "A function maps each input to...", "options": ["Multiple outputs", "Exactly one output", "Zero outputs", "Any output"], "correct": 1, "explanation": "Definition of a function."},
            {"question": "Vertical Line Test checks for...", "options": ["Slope", "Functionality", "Continuity", "Limits"], "correct": 1, "explanation": "If a vertical line hits graph once, it is a function."},
            {"question": "f(x) = x^2. Find f(3).", "options": ["6", "9", "3", "1"], "correct": 1, "explanation": "3 squared is 9."},
            {"question": "Domain refers to...", "options": ["All possible y values", "All possible x values", "The graph itself", "The intercepts"], "correct": 1, "explanation": "Set of allowed inputs."},
            {"question": "Range refers to...", "options": ["All possible inputs", "All possible outputs", "The slope", "The equations"], "correct": 1, "explanation": "Set of possible output values."},
            {"question": "Is a circle a function?", "options": ["Yes", "No", "Sometimes", "Only at origin"], "correct": 1, "explanation": "Fails vertical line test."},
            {"question": "f(x) = 2x. Domain?", "options": ["x > 0", "x < 0", "All real numbers", "Integers only"], "correct": 2, "explanation": "Any number can be multiplied by 2."},
            {"question": "Inverse of f(x) = x + 3 is...", "options": ["x - 3", "3x", "x/3", "-x"], "correct": 0, "explanation": "y = x+3 -> x = y-3 -> f^-1(x) = x-3."},
            {"question": "Composition f(g(x)) means...", "options": ["f times g", "f plus g", "g inside f", "f inside g"], "correct": 2, "explanation": "Apply g first, then f."},
            {"question": "What is f(x) if f(x) = 5?", "options": ["Variable", "Constant function", "Linear", "Quadratic"], "correct": 1, "explanation": "Output is always 5."}
        ],
        "Polynomial and Rational Functions": [
             {"question": "Degree of quadratic polynomial?", "options": ["1", "2", "3", "0"], "correct": 1, "explanation": "Highest power is 2."},
             {"question": "Shape of a quadratic graph?", "options": ["Line", "Circle", "Parabola", "Wave"], "correct": 2, "explanation": "U-shaped curve."},
             {"question": "Roots of x^2 - 4 = 0?", "options": ["2", "-2", "2 and -2", "4"], "correct": 2, "explanation": "(x-2)(x+2)=0."},
             {"question": "Rational function is a ratio of...", "options": ["Two integers", "Two polynomials", "Two lines", "Two circles"], "correct": 1, "explanation": "P(x) / Q(x)."},
             {"question": "Vertical asymptote occurs when denominator is...", "options": ["1", "0", "Positive", "Negative"], "correct": 1, "explanation": "Division by zero is undefined."},
             {"question": "End behavior of x^3?", "options": ["Both up", "Both down", "Down left, Up right", "Up left, Down right"], "correct": 2, "explanation": "Odd degree, positive coefficient."},
             {"question": "Vertex of y = x^2?", "options": ["(0,0)", "(1,1)", "(0,1)", "(1,0)"], "correct": 0, "explanation": "Wait point."},
             {"question": "Factor x^2 + 2x + 1", "options": ["(x+1)(x-1)", "(x+1)^2", "(x-1)^2", "x(x+2)"], "correct": 1, "explanation": "Perfect square trinomial."},
             {"question": "Degree of constant polynomial 5?", "options": ["0", "1", "5", "Undefined"], "correct": 0, "explanation": "x^0."},
             {"question": "Horizontal asymptote compares...", "options": ["Intercepts", "Degrees of numerator/denominator", "Factors", "Roots"], "correct": 1, "explanation": "Determined by highest powers."}
        ],
        "Limits": [
            {"question": "What is a limit?", "options": ["A value function reaches", "A value function approaches", "Maximum value", "Minimum value"], "correct": 1, "explanation": "Behavior near a point."},
            {"question": "Lim x->2 of x+5?", "options": ["2", "5", "7", "10"], "correct": 2, "explanation": "Direct substitution: 2+5."},
            {"question": "Lim x->inf of 1/x?", "options": ["0", "1", "Infinity", "Undefined"], "correct": 0, "explanation": "1 divided by huge number is tiny."},
            {"question": "Indeterminate form?", "options": ["0/0", "1/0", "0/1", "1/1"], "correct": 0, "explanation": "Needs more work (L'Hopital etc)."},
            {"question": "Left hand limit vs Right hand limit", "options": ["Must be different", "Must be equal for limit to exist", "Unrelated", "Always 0"], "correct": 1, "explanation": "Definition of existence."},
            {"question": "Derivative definition uses...", "options": ["Integrals", "Limits", "Geometry", "Algebra"], "correct": 1, "explanation": "Limit of difference quotient."},
            {"question": "Limit of constant c?", "options": ["0", "1", "c", "x"], "correct": 2, "explanation": "Graph is specific height c everywhere."},
            {"question": "Lim x->0 sin(x)/x", "options": ["0", "1", "undefined", "inf"], "correct": 1, "explanation": "Famous limit."},
            {"question": "Continuity requires...", "options": ["Limit exists", "Function defined", "Limit = Function Value", "All of above"], "correct": 3, "explanation": "3-part definition."},
            {"question": "Can a limit exist at a hole?", "options": ["Yes", "No", "Only for lines", "Never"], "correct": 0, "explanation": "Limit describes approach, not arrival."}
        ],
        "Derivatives": [
            {"question": "Derivative represents...", "options": ["Area", "Slope of tangent", "Volume", "Distance"], "correct": 1, "explanation": "Instantaneous rate of change."},
            {"question": "Power Rule: d/dx(x^n) =", "options": ["nx^(n-1)", "x^(n+1)", "nx", "n"], "correct": 0, "explanation": "Bring power down, subtract 1."},
            {"question": "Derivative of sin(x)?", "options": ["cos(x)", "-cos(x)", "tan(x)", "sec(x)"], "correct": 0, "explanation": "Basic trig derivative."},
            {"question": "Derivative of constant?", "options": ["1", "0", "x", "inf"], "correct": 1, "explanation": "No change, slope is 0."},
            {"question": "Product Rule for uv?", "options": ["u'v'", "uv' + vu'", "u'v - uv'", "u/v"], "correct": 1, "explanation": "First d-Second plus Second d-First."},
            {"question": "Chain rule is for...", "options": ["Products", "Quotients", "Composite functions", "Sums"], "correct": 2, "explanation": "Functions inside functions."},
            {"question": "d/dx(e^x)?", "options": ["x*e^x", "e^x", "e", "1"], "correct": 1, "explanation": "It is its own derivative."},
            {"question": "d/dx(ln x)?", "options": ["1/x", "e^x", "x", "1"], "correct": 0, "explanation": "Derivative of natural log."},
            {"question": "Second derivative measures...", "options": ["Velocity", "Concavity/Acceleration", "Jerk", "Position"], "correct": 1, "explanation": "Rate of change of slope."},
            {"question": "Derivative of x is...", "options": ["0", "1", "x", "2"], "correct": 1, "explanation": "Slope of line y=x is 1."}
        ],
        "Applications of Derivatives": [
            {"question": "Critical points occur where f'(x) is...", "options": ["0 or undefined", "Positive", "Negative", "1"], "correct": 0, "explanation": "Potential max/min."},
            {"question": "If f'(x) > 0, f(x) is...", "options": ["Decreasing", "Increasing", "Constant", "Zero"], "correct": 1, "explanation": "Positive slope."},
            {"question": "If f''(x) > 0, graph is...", "options": ["Concave Up", "Concave Down", "Linear", "Flat"], "correct": 0, "explanation": "Like a cup."},
            {"question": "Finding max/min is called...", "options": ["Integration", "Optimization", "Derivation", "Relation"], "correct": 1, "explanation": "Optimizing function value."},
            {"question": "Related Rates use...", "options": ["Time", "Distance", "Mass", "Force"], "correct": 0, "explanation": "d/dt implicit differentiation."},
            {"question": "Mean Value Theorem guarantees...", "options": ["Max", "Min", "Parallel Tangent", "Root"], "correct": 2, "explanation": "Instantaneous slope equals average slope somewhere."},
            {"question": "L'Hopital's Rule handles...", "options": ["Products", "Indeterminate limits", "Integrals", "Series"], "correct": 1, "explanation": "0/0 forms."},
            {"question": "Local max is where...", "options": ["Slope changes + to -", "Slope changes - to +", "Slope is constant", "Slope is infinite"], "correct": 0, "explanation": "Hilltop."},
            {"question": "Inflection point is change in...", "options": ["Slope", "Concavity", "Height", "Domain"], "correct": 1, "explanation": "f''(x) changes sign."},
            {"question": "Velocity is derivative of...", "options": ["Acceleration", "Position", "Time", "Force"], "correct": 1, "explanation": "Change in position."}
        ],
        "Integration": [
            {"question": "Integration is inverse of...", "options": ["Differentiation", "Multiplication", "Addition", "Exponentiation"], "correct": 0, "explanation": "Undoes derivative."},
            {"question": "Definite integral represents...", "options": ["Slope", "Area under curve", "Perimeter", "Volume"], "correct": 1, "explanation": "Net signed area."},
            {"question": "Integral of x^n dx?", "options": ["nx^(n-1)", "x^(n+1)/(n+1)", "x^n", "1/x"], "correct": 1, "explanation": "Reverse power rule."},
            {"question": "+ C represents...", "options": ["Constant of Integration", "Calculus", "Curve", "Circle"], "correct": 0, "explanation": "Indefinite integral family."},
            {"question": "Integral of 1/x dx?", "options": ["ln|x|", "x^-1", "-1/x^2", "e^x"], "correct": 0, "explanation": "Natural log."},
            {"question": "Fundamental Theorem links...", "options": ["Algebra and Geom", "Derivative and Integral", "Limits and Continuity", "Sin and Cos"], "correct": 1, "explanation": "Bridge of calculus."},
            {"question": "U-substitution is... ", "options": ["Reverse Chain Rule", "Reverse Product Rule", "Reverse Quotient", "Reverse Sum"], "correct": 0, "explanation": "Undoes composition."},
            {"question": "Area below x-axis is...", "options": ["Positive", "Negative", "Zero", "Undefined"], "correct": 1, "explanation": "Signed area."},
            {"question": "Integral of e^x?", "options": ["e^x", "x*e^x", "ln x", "1"], "correct": 0, "explanation": "Own integral."},
            {"question": "Integral of cos(x)", "options": ["sin(x)", "-sin(x)", "tan(x)", "sec(x)"], "correct": 0, "explanation": "Deriv of sin is cos."}
        ],

        # --- PHYSICS ---
        "Units and Measurement": [
            {"question": "SI unit for length?", "options": ["Inch", "Meter", "Mile", "Foot"], "correct": 1, "explanation": "m is standard."},
            {"question": "SI unit for time?", "options": ["Hour", "Minute", "Second", "Day"], "correct": 2, "explanation": "s."},
            {"question": "SI unit for mass?", "options": ["Gram", "Pound", "Kilogram", "Ton"], "correct": 2, "explanation": "kg."},
            {"question": "Prefix 'kilo' means...", "options": ["100", "1000", "0.1", "0.001"], "correct": 1, "explanation": "10^3."},
            {"question": "Prefix 'milli' means...", "options": ["1000", "0.1", "0.01", "0.001"], "correct": 3, "explanation": "10^-3."},
            {"question": "How many seconds in an hour?", "options": ["60", "3600", "100", "1000"], "correct": 1, "explanation": "60*60."},
            {"question": "Dimensional analysis checks...", "options": ["Numbers", "Units", "Colors", "Spelling"], "correct": 1, "explanation": "Validity of equations."},
            {"question": "Significant figures measure...", "options": ["Precision", "Accuracy", "Size", "Weight"], "correct": 0, "explanation": "Reliability of digits."},
            {"question": "Convert 100cm to m.", "options": ["1m", "10m", "0.1m", "0.01m"], "correct": 0, "explanation": "100cm = 1m."},
            {"question": "Scalar has...", "options": ["Magnitude only", "Direction only", "Both", "Neither"], "correct": 0, "explanation": "Unlike vectors."}
        ],
        "Vectors": [
            {"question": "Vector has...", "options": ["Magnitude only", "Direction only", "Magnitude and Direction", "Color"], "correct": 2, "explanation": "Arrow with length and direction."},
            {"question": "Velocity is a...", "options": ["Scalar", "Vector", "Number", "Unit"], "correct": 1, "explanation": "Speed + Direction."},
            {"question": "Adding vectors tip-to-tail finds...", "options": ["Resultant", "Difference", "Product", "Quotient"], "correct": 0, "explanation": "Geometric addition."},
            {"question": "Unit vector has magnitude...", "options": ["0", "1", "10", "Infinite"], "correct": 1, "explanation": "Length 1."},
            {"question": "Dot product results in...", "options": ["Vector", "Scalar", "Matrix", "Zero"], "correct": 1, "explanation": "Number."},
            {"question": "Cross product results in...", "options": ["Vector", "Scalar", "Matrix", "Zero"], "correct": 0, "explanation": "Perpendicular vector."},
            {"question": "Component form of vector", "options": ["(x, y)", "x+y", "x/y", "x*y"], "correct": 0, "explanation": "x and y parts."},
            {"question": "Magnitude of vector (3,4)?", "options": ["7", "1", "5", "12"], "correct": 2, "explanation": "sqrt(3^2 + 4^2) = 5."},
            {"question": "Direction is often measrued by...", "options": ["Angle", "Length", "Size", "Color"], "correct": 0, "explanation": "Angle from axis."},
            {"question": "Zero vector has magnitude...", "options": ["0", "1", "-1", "inf"], "correct": 0, "explanation": "Length 0."}
        ],
        "Motion Along a Straight Line": [
            {"question": "Displacement is...", "options": ["Total path length", "Change in position", "Speed", "Time"], "correct": 1, "explanation": "Final - Initial."},
            {"question": "Average velocity is...", "options": ["Dist/Time", "Disp/Time", "Speed/Time", "Accel/Time"], "correct": 1, "explanation": "Displacement over time."},
            {"question": "Slope of position-time graph?", "options": ["Velocity", "Acceleration", "Displacement", "Jerk"], "correct": 0, "explanation": "Rate of change of position."},
            {"question": "Slope of velocity-time graph?", "options": ["Velocity", "Acceleration", "Displacement", "Jerk"], "correct": 1, "explanation": "Rate of change of velocity."},
            {"question": "Acceleration due to gravity (earth)", "options": ["9.8 m/s^2", "10 m/s", "32 m/s", "5 m/s^2"], "correct": 0, "explanation": "Approx 9.8."},
            {"question": "Area under velocity-time graph?", "options": ["Acceleration", "Displacement", "Speed", "Force"], "correct": 1, "explanation": "Integration involves time."},
            {"question": "Free fall ignores...", "options": ["Gravity", "Air resistance", "Mass", "Time"], "correct": 1, "explanation": "Idealized model."},
            {"question": "Instantaneous speed is magnitude of...", "options": ["Instantaneous velocity", "Average velocity", "Acceleration", "Force"], "correct": 0, "explanation": "Speed at exact moment."},
            {"question": "If accel is 0, velocity is...", "options": ["0", "Constant", "Increasing", "Decreasing"], "correct": 1, "explanation": "No change."},
            {"question": "Equation v = v0 + at apples for...", "options": ["Constant accel", "Variable accel", "Zero velocity", "No gravity"], "correct": 0, "explanation": "Constant acceleration formula."}
        ],
        "Newton's Laws of Motion": [
             {"question": "1st Law deals with...", "options": ["Inertia", "Force", "Action/Reaction", "Gravity"], "correct": 0, "explanation": "Resistance to change."},
             {"question": "2nd Law Formula?", "options": ["F=m/a", "F=ma", "F=m+a", "F=a/m"], "correct": 1, "explanation": "Force = mass * acceleration."},
             {"question": "3rd Law: Action and Reaction are...", "options": ["Equal and Opposite", "Unequal", "Parallel", "Unrelated"], "correct": 0, "explanation": "Equal magnitude, opposite direction."},
             {"question": "Unit of Force?", "options": ["Joule", "Watt", "Newton", "Pascal"], "correct": 2, "explanation": "N."},
             {"question": "Mass is measure of...", "options": ["Weight", "Inertia", "Volume", "Density"], "correct": 1, "explanation": "Stuff in object."},
             {"question": "Weight depends on...", "options": ["Gravity", "Shape", "Color", "Speed"], "correct": 0, "explanation": "W = mg."},
             {"question": "Normal force is...", "options": ["Parallel to surface", "Perpendicular to surface", "Downward", "Upward"], "correct": 1, "explanation": "Support force."},
             {"question": "Friction acts...", "options": ["In direction of motion", "Opposite to motion", "Perpendicular", "Downward"], "correct": 1, "explanation": "Resists motion."},
             {"question": "Net force of 0 means...", "options": ["Zero Velocity", "Constant Velocity", "High Acceleration", "Stopping"], "correct": 1, "explanation": "Equilibrium."},
             {"question": "Tension is force in...", "options": ["Spring", "Rope/String", "Surface", "Fluid"], "correct": 1, "explanation": "Pulling force."}
        ],
         "Thermodynamics": [
            {"question": "Unit of Temperature?", "options": ["Kelvin", "Newton", "Joule", "Watt"], "correct": 0, "explanation": "SI unit is K."},
            {"question": "Absolute Zero is...", "options": ["0 C", "-273.15 C", "32 F", "100 C"], "correct": 1, "explanation": "0 Kelvin."},
            {"question": "Heat flows from...", "options": ["Cold to Hot", "Hot to Cold", "Low to High", "Nowhere"], "correct": 1, "explanation": "2nd Law."},
            {"question": "1st Law of Thermo is...", "options": ["Conservation of Energy", "Entropy", "Equilibrium", "Zero"], "correct": 0, "explanation": "Energy not created/destroyed."},
            {"question": "Entropy measures...", "options": ["Energy", "Disorder", "Heat", "Work"], "correct": 1, "explanation": "Randomness."},
            {"question": "PV = nRT is...", "options": ["Ideal Gas Law", "Newton Law", "Ohm Law", "Boyle Law"], "correct": 0, "explanation": "Gas equation."},
            {"question": "Conduction needs...", "options": ["Contact", "Fluid", "Vacuum", "Light"], "correct": 0, "explanation": "Direct touch."},
            {"question": "Convection happens in...", "options": ["Solids", "Fluids", "Vacuum", "Space"], "correct": 1, "explanation": "Liquids/Gases."},
            {"question": "Radiation needs...", "options": ["Medium", "No Medium", "Solid", "Liquid"], "correct": 1, "explanation": "travels through vacuum."},
            {"question": "Specific heat capacity?", "options": ["Energy to melt", "Energy to raise temp", "Energy to boil", "Total energy"], "correct": 1, "explanation": "Heat to raise 1kg by 1K."}
        ],
        "Electricity and Magnetism": [
            {"question": "Unit of Charge?", "options": ["Ampere", "Coulomb", "Volt", "Ohm"], "correct": 1, "explanation": "C."},
            {"question": "Like charges...", "options": ["Attract", "Repel", "Ignore", "Spin"], "correct": 1, "explanation": "Push away."},
            {"question": "Ohm's Law?", "options": ["V=IR", "F=ma", "E=mc^2", "P=IV"], "correct": 0, "explanation": "Volt = Current * Resist."},
            {"question": "Unit of Resistance?", "options": ["Volt", "Amp", "Ohm", "Watt"], "correct": 2, "explanation": "Omega."},
            {"question": "Current is flow of...", "options": ["Protons", "Neutrons", "Electrons", "Atoms"], "correct": 2, "explanation": "Charge carriers."},
            {"question": "Magnetic field created by...", "options": ["Stationary charge", "Moving charge", "Neutrons", "Heat"], "correct": 1, "explanation": "Current makes B-field."},
            {"question": "AC stands for...", "options": ["Alternating Current", "Anti Current", "After Current", "Air Cond"], "correct": 0, "explanation": "Changes direction."},
            {"question": "Capacitor stores...", "options": ["Current", "Energy field", "Heat", "Light"], "correct": 1, "explanation": "Electric field."},
            {"question": "Inductor opposes change in...", "options": ["Voltage", "Current", "Resistance", "Capacitance"], "correct": 1, "explanation": "Magnetic inertia."},
            {"question": "Speed of EM wave?", "options": ["Speed of sound", "Speed of light", "Infinite", "0"], "correct": 1, "explanation": "c."}
        ],
        "Optics": [
            {"question": "Light behaves as...", "options": ["Particle", "Wave", "Both", "Neither"], "correct": 2, "explanation": "Duality."},
            {"question": "Reflection angle equals...", "options": ["Refraction angle", "Incident angle", "90 deg", "0"], "correct": 1, "explanation": "Law of Reflection."},
            {"question": "Refraction is...", "options": ["Bouncing", "Bending", "Stopping", "Splitting"], "correct": 1, "explanation": "Bending light."},
            {"question": "Speed of light in vacuum?", "options": ["3x10^8 m/s", "300 m/s", "1000 m/s", "Instant"], "correct": 0, "explanation": "c."},
            {"question": "Concave mirror focuses light to...", "options": ["Center", "Focal point", "Infinity", "Surface"], "correct": 1, "explanation": "Converging."},
            {"question": "Convex lens is...", "options": ["Diverging", "Converging", "Flat", "Opaque"], "correct": 1, "explanation": "Thicker in middle."},
            {"question": "Snell's Law relates...", "options": ["Angles and Indices", "Force and Mass", "V and I", "Heat and Temp"], "correct": 0, "explanation": "n1sin1 = n2sin2."},
            {"question": "Prism causes...", "options": ["Dispersion", "Fusion", "Fission", "Collision"], "correct": 0, "explanation": "Splits colors."},
            {"question": "Primary colors of light?", "options": ["RYB", "RGB", "CMY", "BW"], "correct": 1, "explanation": "Red Green Blue."},
            {"question": "Myopia is...", "options": ["Farsightedness", "Nearsightedness", "Blindness", "Colorblind"], "correct": 1, "explanation": "Can't see far."}
        ],

        # --- PYTHON ---
        "Variables": [
            {"question": "Valid variable name?", "options": ["2var", "_var", "var-2", "class"], "correct": 1, "explanation": "Starts with _ or letter."},
            {"question": "Assignment operator?", "options": ["==", "=", "===", ":"], "correct": 1, "explanation": "Single =."},
            {"question": "Dynamic typing means...", "options": ["Type fixed", "Type changes", "Type error", "No types"], "correct": 1, "explanation": "Python infers type."},
            {"question": "x = 5; x is type...", "options": ["float", "int", "str", "bool"], "correct": 1, "explanation": "Integer."},
            {"question": "x = '5'; x is type...", "options": ["float", "int", "str", "bool"], "correct": 2, "explanation": "String."},
            {"question": "Convert '5' to int?", "options": ["int('5')", "str(5)", "float('5')", "num('5')"], "correct": 0, "explanation": "Casting."},
            {"question": "Swap variables a,b?", "options": ["a=b", "a,b = b,a", "swap(a,b)", "b=a"], "correct": 1, "explanation": "Tuple unpacking."},
            {"question": "Global variable is defined...", "options": ["Inside func", "Outside func", "In loop", "Nowhere"], "correct": 1, "explanation": "Scope."},
            {"question": "Constant convention?", "options": ["lowercase", "UPPERCASE", "CamelCase", "snake_case"], "correct": 1, "explanation": "ALL_CAPS."},
            {"question": "del x does what?", "options": ["Prints x", "Deletes x", "Saves x", "Nothing"], "correct": 1, "explanation": "Removes from memory."}
        ],
        "Loops": [
            {"question": "Which is a loop?", "options": ["if", "for", "def", "class"], "correct": 1, "explanation": "Iteration."},
            {"question": "range(3) produces...", "options": ["1,2,3", "0,1,2", "0,1,2,3", "3,3,3"], "correct": 1, "explanation": "Start 0, excl stop."},
            {"question": "Stop a loop with...", "options": ["stop", "break", "exit", "continue"], "correct": 1, "explanation": "Break statement."},
            {"question": "Skip iteration with...", "options": ["skip", "break", "continue", "pass"], "correct": 2, "explanation": "Continue statement."},
            {"question": "While loop runs until...", "options": ["True", "False", "Forever", "Error"], "correct": 1, "explanation": "Condition false."},
            {"question": "Iterate list items?", "options": ["for x in list:", "loop list:", "while list:", "if list:"], "correct": 0, "explanation": "For-in syntax."},
            {"question": "Indentation in loops...", "options": ["Optional", "Required", "Ignored", "Forbidden"], "correct": 1, "explanation": "Defines block."},
            {"question": "Infinite loop happens when...", "options": ["Condition never True", "Condition never False", "Computer breaks", "Always"], "correct": 1, "explanation": "Never exits."},
            {"question": "Nested loop is...", "options": ["Loop in loop", "Loop outside", "Broken loop", "Fast loop"], "correct": 0, "explanation": "Inner/Outer."},
            {"question": "enumerate gives...", "options": ["Index only", "Value only", "Index and Value", "Nothing"], "correct": 2, "explanation": "Tuple (i, v)."}
        ],
        "Functions": [
            {"question": "Define function keyword?", "options": ["func", "def", "function", "define"], "correct": 1, "explanation": "def name():"},
            {"question": "Return data with...", "options": ["send", "return", "output", "print"], "correct": 1, "explanation": "Return statement."},
            {"question": "Docstring purpose?", "options": ["Execute code", "Document code", "Import code", "Speed up"], "correct": 1, "explanation": "Documentation."},
            {"question": "Values passed to func are...", "options": ["Arguments", "Loops", "Classes", "Strings"], "correct": 0, "explanation": "Inputs."},
            {"question": "Default argument?", "options": ["def f(a=1):", "def f(a):", "def f(a==1):", "def f(*a):"], "correct": 0, "explanation": "Preset value."},
            {"question": "*args allows...", "options": ["1 arg", "Variable args", "No args", "Keyword args"], "correct": 1, "explanation": "Tuple of args."},
            {"question": "**kwargs allows...", "options": ["List args", "Keyword args", "No args", "Int args"], "correct": 1, "explanation": "Dict of named args."},
            {"question": "Lambda is...", "options": ["Big function", "Anonymous function", "Class", "Module"], "correct": 1, "explanation": "Small inline func."},
            {"question": "Recursive function calls...", "options": ["Main", "Itself", "Print", "Exit"], "correct": 1, "explanation": "Recursion."},
            {"question": "Scope of var in func?", "options": ["Global", "Local", "Universal", "None"], "correct": 1, "explanation": "Local scope."}
        ],
        "Classes": [
            {"question": "Blueprint for object?", "options": ["List", "Class", "Func", "Loop"], "correct": 1, "explanation": "Definition."},
            {"question": "Create instance?", "options": ["Class()", "new Class", "Class.new", "make Class"], "correct": 0, "explanation": "Call class like func."},
            {"question": "__init__ is...", "options": ["Terminator", "Constructor", "Loop", "Import"], "correct": 1, "explanation": "Initializer."},
            {"question": "'self' refers to...", "options": ["The class", "The instance", "Global", "Python"], "correct": 1, "explanation": "Current object."},
            {"question": "Inheritance allows...", "options": ["Copying code", "Extending classes", "Deleting classes", "Hiding classes"], "correct": 1, "explanation": "Child gets Parent traits."},
            {"question": "Parent class also called...", "options": ["Super class", "Sub class", "Mini class", "Mega class"], "correct": 0, "explanation": "Super."},
            {"question": "Method is...", "options": ["Variable in class", "Function in class", "List in class", "Import"], "correct": 1, "explanation": "Behavior."},
            {"question": "Attribute is...", "options": ["Data of object", "Code of object", "Name of file", "Error"], "correct": 0, "explanation": "Field/Variable."},
            {"question": "Polymorphism means...", "options": ["Many forms", "One form", "No form", "Shape shift"], "correct": 0, "explanation": "Same method, diff behavior."},
            {"question": "__str__ used for...", "options": ["Math", "String representation", "Looping", "Init"], "correct": 1, "explanation": "Printable string."}
        ]
    }
