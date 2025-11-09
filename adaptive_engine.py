"""
adaptive_engine.py — Adjusts question difficulty based on learner performance.

Implements a simple *rule-based* adaptive system:
- Increases difficulty if the learner is accurate and fast
- Decreases difficulty if accuracy is low or responses are slow
- Otherwise, keeps the same level
"""

LEVELS = ['Easy', 'Medium', 'Hard']
TIME_THRESHOLDS = {'Easy': 8.0, 'Medium': 12.0, 'Hard': 20.0}


class AdaptiveEngine:
    """Encapsulates logic for adaptive difficulty adjustment."""

    def __init__(self, window_min=3):
        # Minimum number of recent trials before changing difficulty
        self.window_min = window_min

    def _level_index(self, level):
        """Return numeric index of a level ('Easy' → 0, 'Medium' → 1, 'Hard' → 2)."""
        return LEVELS.index(level)

    def next_level(self, current_level, tracker):
        """
        Determine the next difficulty level based on recent performance.

        Rules:
        - If accuracy ≥ 0.8 and avg time ≤ threshold → increase difficulty
        - If accuracy ≤ 0.5 or avg time ≥ 1.5× threshold → decrease difficulty
        - Otherwise, stay at current level
        """
        recent_acc = tracker.recent_accuracy()
        recent_time = tracker.recent_avg_time()

        # Not enough recent data yet → no change
        if recent_acc is None or len(tracker.window) < self.window_min:
            return current_level

        time_thr = TIME_THRESHOLDS[current_level]

        # Increase difficulty (learner doing well)
        if recent_acc >= 0.8 and recent_time <= time_thr:
            idx = self._level_index(current_level)
            return LEVELS[min(idx + 1, len(LEVELS) - 1)]

        # Decrease difficulty (learner struggling)
        if recent_acc <= 0.5 or recent_time >= time_thr * 1.5:
            idx = self._level_index(current_level)
            return LEVELS[max(idx - 1, 0)]

        # Otherwise, stay at the same difficulty
        return current_level

    # -------------------------------------------------------------------------
    # (Optional) ML-BASED EXTENSION
    # -------------------------------------------------------------------------
    def ml_predict_next(self, features, model):
        """
        Optional ML-based adaptation stub.
        Given input features and a trained scikit-learn model,
        predict whether to move difficulty up (+1), down (-1), or stay (0).
        """
        return model.predict([features])[0]
