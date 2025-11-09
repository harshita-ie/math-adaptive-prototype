#!/usr/bin/env python3
"""
main.py — Entry point for the Adaptive Math Learning Prototype.

This script runs a console-based adaptive learning session.
It interacts with:
    - PuzzleGenerator: generates math problems
    - Tracker: records performance (accuracy, speed)
    - AdaptiveEngine: adjusts difficulty based on performance

Author: (Your Name)
"""

import time
from puzzle_generator import PuzzleGenerator
from tracker import Tracker
from adaptive_engine import AdaptiveEngine


def choose_initial_level():
    """
    Prompt the learner to choose an initial difficulty level.
    Returns: 'Easy', 'Medium', or 'Hard'
    """
    while True:
        choice = input('Choose initial difficulty (Easy/Medium/Hard) [Easy]: ').strip().lower()
        if choice == '':
            # Default to Easy if user just presses Enter
            return 'Easy'
        if choice in ('easy', 'medium', 'hard'):
            return choice.capitalize()
        print('Please type Easy, Medium or Hard.')


def run_session():
    """
    Run one full adaptive learning session in the console.
    Handles:
      - User interaction loop
      - Puzzle presentation
      - Answer checking
      - Performance tracking
      - Adaptive difficulty adjustment
    """
    # Step 1: Get learner name and initial difficulty
    name = input('Enter learner name: ').strip() or 'Learner'
    level = choose_initial_level()

    print(f'\nHello {name}! Starting session at {level} level.')
    print('Type "quit" anytime to stop.\n')

    # Step 2: Initialize components
    pg = PuzzleGenerator()  # Generates questions
    tracker = Tracker()     # Logs performance
    engine = AdaptiveEngine()  # Determines next difficulty

    current_level = level  # start difficulty

    # Step 3: Main learning loop
    while True:
        # --- Generate a new problem ---
        q, ans = pg.generate(current_level)

        # --- Display question ---
        print(f'Level: {current_level} | Question: {q} = ?')

        # --- Measure response time ---
        start = time.time()
        resp = input('> ').strip()

        # --- Exit condition ---
        if resp.lower() in ('quit', 'exit'):
            break

        # --- Parse user input ---
        try:
            user_ans = float(resp)
        except:
            # If invalid input (like text), count as incorrect
            print('Invalid answer (enter a number). Counted as incorrect.')
            user_ans = None

        elapsed = time.time() - start  # total time spent answering

        # --- Check correctness ---
        correct = (user_ans is not None and abs(user_ans - ans) < 1e-6)

        # --- Record the result ---
        tracker.log_trial(
            question=q,
            correct=correct,
            response_time=elapsed,
            difficulty=current_level
        )

        # --- Adaptive difficulty adjustment ---
        next_level = engine.next_level(current_level, tracker)

        # If the difficulty changed, notify the learner
        if next_level != current_level:
            print(f'>> Difficulty changed: {current_level} → {next_level}\n')

        current_level = next_level  # update level for next round

    # Step 4: Print final summary and stats
    print('\nSession ended. Summary:')
    summary = tracker.session_summary()
    print(summary)
    print('\nGoodbye, and keep learning!')


# Standard Python entry point
if __name__ == '__main__':
    run_session()
