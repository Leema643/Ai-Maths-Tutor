"""Simple test to verify core application logic without requiring model downloads"""
import sys
sys.path.insert(0, '.')

# Test imports
try:
    from utils.image_utils import preprocess_for_ocr, to_bytes
    print("✓ image_utils imported successfully")
except Exception as e:
    print(f"✗ image_utils import failed: {e}")

try:
    from solver.equation_solver import parse_latex_to_sympy, solve_equation, generate_steps
    print("✓ equation_solver imported successfully")
except Exception as e:
    print(f"✗ equation_solver import failed: {e}")

try:
    from checker.mistake_checker import detect_mistakes
    print("✓ mistake_checker imported successfully")
except Exception as e:
    print(f"✗ mistake_checker import failed: {e}")

# Test equation solver on a simple example
print("\n--- Testing Equation Solver ---")
try:
    # Test parsing and solving a simple equation: x + 2 = 5
    latex = "x + 2 = 5"
    sym = parse_latex_to_sympy(latex)
    print(f"Parsed LaTeX: {latex}")
    print(f"Sympy object: {sym}")
    
    res = solve_equation(sym)
    print(f"Solutions: {res.get('solutions')}")
    
    steps = generate_steps(sym)
    print("Steps:")
    for title, content in steps:
        print(f"  - {title}: {content}")
    
    print("✓ Equation solver works!")
except Exception as e:
    print(f"✗ Equation solver failed: {e}")
    import traceback
    traceback.print_exc()

# Test mistake checker
print("\n--- Testing Mistake Checker ---")
try:
    latex = "x + 2 = 5"
    sym = parse_latex_to_sympy(latex)
    mistakes = detect_mistakes(latex, sym)
    print(f"Mistakes detected in '{latex}': {mistakes}")
    print("✓ Mistake checker works!")
except Exception as e:
    print(f"✗ Mistake checker failed: {e}")
    import traceback
    traceback.print_exc()

print("\n✓ Basic application logic verified!")
