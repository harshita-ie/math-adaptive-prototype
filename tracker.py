"""
tracker.py — Tracks learner performance during a session.

Logs:
- Each question asked
- Whether it was answered correctly
- Response time
- Difficulty level

Provides:
- Recent accuracy and speed (for adaptive logic)
- Overall session statistics
"""

import time
from collections import deque


class Tracker:
    """Keeps a log of the learner’s performance and computes useful metrics."""

    def __init__(self, window_size=5):
        self.trials = []  # Full session history
        self.window = deque(maxlen=window_size)  # Recent trials (sliding window)
        self.window_size = window_size

    def log_trial(self, question, correct, response_time, difficulty):
        """
        Record one trial (single question) in memory.
        Each record stores question text, correctness, time taken, and difficulty.
        """
        record = {
            'question': question,
            'correct': bool(correct),
            'response_time': float(response_time),
            'difficulty': difficulty,
            'timestamp': time.time()
        }
        self.trials.append(record)
        self.window.append(record)

    # -------------------------------------------------------------------------
    # RECENT PERFORMANCE METRICS
    # -------------------------------------------------------------------------
    def recent_accuracy(self):
        """Return accuracy over recent trials (sliding window)."""
        if not self.window:
            return None
        return sum(1 for t in self.window if t['correct']) / len(self.window)

    def recent_avg_time(self):
        """Return average response time over recent trials."""
        if not self.window:
            return None
        return sum(t['response_time'] for t in self.window) / len(self.window)

    # -------------------------------------------------------------------------
    # OVERALL SESSION METRICS
    # -------------------------------------------------------------------------
    def total_accuracy(self):
        """Return accuracy over the entire session."""
        if not self.trials:
            return 0.0
        return sum(1 for t in self.trials if t['correct']) / len(self.trials)

    def avg_time(self):
        """Return average response time over the entire session."""
        if not self.trials:
            return 0.0
        return sum(t['response_time'] for t in self.trials) / len(self.trials)

    def session_summary(self):
        """
        Return a summary dictionary of performance stats.
        Useful for printing at the end of the session.
        """
        return {
            'total_trials': len(self.trials),
            'accuracy': self.total_accuracy(),
            'avg_time': self.avg_time(),
            'trials': self.trials[-20:]  # include last 20 trials for review
        }
