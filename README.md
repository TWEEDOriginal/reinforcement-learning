# Project 2: Reinforcement Learning - Code Modifications

## Overview
This project involved implementing agents that solve Markov Decision Processes (MDPs) using Value Iteration and Q-Learning techniques. We modified three main files:

- `valueIterationAgents.py`: for implementing Value Iteration
- `qlearningAgents.py`: for implementing Q-Learning and Approximate Q-Learning
- `analysis.py`: for parameter tuning of the Gridworld environment

---

## 1. Modifications in `valueIterationAgents.py`

We completed the implementation of the `ValueIterationAgent` class:

### Methods Implemented

- **`runValueIteration`**:  
  Runs batch value iteration for the given number of iterations using the Bellman update equation. Values are updated using a separate copy (`newValues`) to avoid in-place updates.

- **`computeQValueFromValues(state, action)`**:  
  Computes the Q-value for a `(state, action)` pair using the current value function.

- **`computeActionFromValues(state)`**:  
  Returns the best action based on the current value estimates by selecting the action that yields the highest Q-value.

---

## 2. Modifications in `qlearningAgents.py`

We implemented two agents: `QLearningAgent` and `ApproximateQAgent`.

### `QLearningAgent` Methods

- **`getQValue(state, action)`**:  
  Returns Q-values stored in a `util.Counter`, defaulting to 0.0 for unseen (state, action) pairs.

- **`computeValueFromQValues(state)`**:  
  Computes the maximum Q-value over all legal actions in a given state.

- **`computeActionFromQValues(state)`**:  
  Returns the best action based on current Q-values, breaking ties randomly.

- **`getAction(state)`**:  
  Implements epsilon-greedy action selection: with probability `epsilon` chooses a random action; otherwise, chooses the best known action.

- **`update(state, action, nextState, reward)`**:  
  Performs the Q-learning update rule to adjust the Q-value of the current `(state, action)` pair.

### `ApproximateQAgent` Methods

- **`__init__`**:  
  Initializes the feature extractor and weight counter.

- **`getQValue(state, action)`**:  
  Calculates Q-values as a dot product between features and learned weights.

- **`update(state, action, nextState, reward)`**:  
  Updates feature weights using the difference between the predicted and target Q-values.

- **`final(state)` (optional)**:  
  Displays final weights after training is complete.

---

## 3. Modifications in `analysis.py`

We implemented functions `question3a()` through `question3e()` to return specific parameter settings for the `DiscountGrid` environment.

Each function returns a tuple of:
- **Discount factor**
- **Noise**
- **Living reward**

These were tuned to encourage different policies (e.g., risk-taking, avoiding the cliff, preferring distant rewards, or avoiding all exits).

---

## Testing and Evaluation

Each question was tested using the autograder:

```bash
python autograder.py -q q1
python autograder.py -q q2
...
python autograder.py -q q6
