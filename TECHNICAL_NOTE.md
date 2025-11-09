# Technical Note — Math Adventures Adaptive Prototype

## Architecture / Flow
- **main.py**: Console UI loop. Handles user name, initial difficulty selection, session loop (presents puzzles, records answers), and prints summary.
- **puzzle_generator.py**: Generates math problems for three difficulty levels (Easy, Medium, Hard) and for four operations (add, subtract, multiply, divide).
- **tracker.py**: Keeps an in-memory log of each trial: question, correct answer, user's answer, correctness, and response time. Exposes convenience methods to compute accuracy and average response time over a sliding window.
- **adaptive_engine.py**: Implements the adaptive logic. Default is rule-based using recent performance (window of last N trials). An ML-mode stub is included that can be trained on simulated data (uses scikit-learn logistic regression) to predict next difficulty if desired.

## Adaptive Logic (Rule-based)
We chose a **rule-based engine** for this prototype because it is:
- Simple to implement and explain (good for a demo and grading emphasis on reasoning).
- Robust to small datasets and noisy early-stage interactions.
- Deterministic and easy to debug during demonstrations.

Rules (applied after each trial, using a sliding window of size 5):
- If accuracy ≥ 0.8 **and** average response time ≤ time_threshold_for_level → increase difficulty by one level (up to Hard).
- If accuracy ≤ 0.5 **or** average response time ≥ time_threshold_for_level * 1.5 → decrease difficulty by one level (down to Easy).
- Otherwise, keep the same difficulty.

Time thresholds by level (approximate):
- Easy: 8s, Medium: 12s, Hard: 20s.

## Metrics Tracked
- Trial-level: correctness (bool), response time (seconds), difficulty, operation, operands.
- Session-level: overall accuracy, average response time, counts of difficulty transitions.
These metrics directly influence the rule-based adaptation above (accuracy and response time steer difficulty up/down).

## Why this approach?
- The assignment emphasizes **adaptive logic** over UI. A rule-based approach clearly demonstrates how adaptation happens and why.
- ML-driven adaptation requires labeled historical data. For a small prototype, rule-based provides immediate, interpretable personalization.
- We include an ML stub so instructors can extend the prototype using simulated or collected data later.

## How to collect data to train/improve a model
- Log all session trials to a central datastore (CSV, database) with fields: user_id, timestamp, difficulty, operation, operands, correct (0/1), response_time.
- Use this logged history to train a classifier/regressor that predicts probability of correct response for a given candidate difficulty; choose the difficulty that keeps predicted success probability in a target range (e.g., 0.6–0.85).
- Use cross-validation, regularization, and features like prior accuracy, time trends, and per-operation performance.

## Handling noisy/inconsistent performance
- Use smoothing (e.g., exponential moving average) over recent trials to avoid reacting to single lucky/unlucky answers.
- Require a minimum number of trials before making a difficulty change (we use a short sliding window of 5).
- Incorporate response time as complementary signal — long correct answers may indicate the problem is still too hard.

## Trade-offs: Rule-based vs ML-driven
- **Rule-based**: Simple, interpretable, low data needs, easier to justify to educators. But may be rigid and not capture subtle patterns.
- **ML-driven**: Can personalize based on many signals and adapt over time, but requires data, careful validation, and is less interpretable.

## Scaling beyond math
- Abstract puzzles to "problems" with features (topic, subskill, difficulty scalar). The adaptive engine can be reused to target specific skills.
- Track per-skill metrics and route learners to focused practice modules.

---
This technical note is intentionally concise (1–2 pages). For more, extend this file into a report or record a short demo video showing the prototype in action.
