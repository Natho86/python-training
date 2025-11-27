# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Purpose

This is a Python training exercises repository designed to create a comprehensive set of progressive exercises from beginner to intermediate level. The specification is in `python_training_exercises.md`.

## Repository State

This repository is currently in the planning phase. The directory structure and exercise files have not yet been created. The specification document defines:
- 50 exercises organized by difficulty (Beginner, Beginner+, Intermediate-, Intermediate)
- A three-phase progression system
- Specific directory structure requirements
- Exercise format templates

## Project Structure (To Be Created)

The specification requires this structure:
```
python_training/
├── README.md
├── beginner/
│   └── 01_to_15_fundamentals/
├── intermediate/
│   ├── 16_to_30_building_skills/
│   └── 31_to_50_advanced/
├── projects/
│   ├── beginner_projects/
│   └── intermediate_projects/
└── resources/
```

## Exercise File Format

Each exercise follows a strict template structure defined in `python_training_exercises.md`:
- **Exercise file**: Contains problem statement, hints, and example I/O
- **Solution file**: Contains complete solution with detailed explanation
- Both files must include: title, difficulty, concepts covered, and extension challenges

### Exercise Naming Convention
- Exercise files: `exercise_01.py`, `exercise_02.py`, etc.
- Solution files: `exercise_01_solution.py`, `exercise_02_solution.py`, etc.

## Development Guidelines

### Code Standards
- Python 3.x compatible
- Follow PEP 8 style guidelines
- Include docstrings for all functions
- Use meaningful variable names
- Add comments for complex logic
- Test all solutions before committing

### Exercise Creation Requirements
1. Each exercise must include: title, difficulty level, concepts covered, problem statement, example I/O, 2-3 hints, solution, explanation, and extension challenge
2. Exercises must follow the progression path defined in the specification
3. Solutions must be complete, working, and well-explained
4. Focus on practical, engaging problems that build on previous concepts

## Topic Progression

### Phase 1 (Exercises 1-15): Beginner Fundamentals
Variables, data types, control flow, loops, basic data structures (lists), function basics

### Phase 2 (Exercises 16-30): Building Skills
Dictionaries, tuples, sets, string operations, list comprehensions, file I/O, error handling

### Phase 3 (Exercises 31-50): Intermediate Concepts
Advanced functions (*args/**kwargs, lambdas, decorators), OOP (classes, inheritance), modules, JSON, data processing

## Testing Exercises

Since no test framework is specified, manually test each solution by:
1. Running the solution file: `python3 path/to/exercise_XX_solution.py`
2. Verifying output matches expected results
3. Testing edge cases mentioned in the problem statement
4. Ensuring code handles invalid inputs gracefully (where appropriate)

## Creating New Exercises

When generating exercises:
1. Review the specification in `python_training_exercises.md` to understand requirements
2. Ensure the exercise fits the appropriate difficulty level and phase
3. Build on concepts from previous exercises in the sequence
4. Include both the problem file and solution file
5. Make sure hints are helpful without revealing the solution
6. Write explanations that teach concepts, not just describe the code
