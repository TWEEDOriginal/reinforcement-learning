# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    answerDiscount = 0.9
    answerNoise = 0.0  # No noise means the agent will take the optimal path without risk
    return answerDiscount, answerNoise

def question3a():
    # Prefer the close exit (+1), risking the cliff (-10)
    answerDiscount = 0.1  # Low discount makes agent prefer immediate reward
    answerNoise = 0.0     # No noise means it will take the risky path
    answerLivingReward = 0.0  # No living reward means no penalty for taking longer paths
    return answerDiscount, answerNoise, answerLivingReward

def question3b():
    # Prefer the close exit (+1), but avoiding the cliff (-10)
    answerDiscount = 0.3   # Higher discount than 3a but still prefers closer reward
    answerNoise = 0.2      # Some noise makes the risky path less attractive
    answerLivingReward = 0.0  # No living reward
    return answerDiscount, answerNoise, answerLivingReward

def question3c():
    # Prefer the distant exit (+10), risking the cliff (-10)
    answerDiscount = 0.9   # High discount makes agent value distant reward
    answerNoise = 0.0      # No noise means it will take the risky path
    answerLivingReward = 0.0  # No living reward
    return answerDiscount, answerNoise, answerLivingReward

def question3d():
    # Prefer the distant exit (+10), avoiding the cliff (-10)
    answerDiscount = 0.9   # High discount makes agent value distant reward
    answerNoise = 0.2      # Some noise makes the risky path less attractive
    answerLivingReward = 0.0  # No living reward
    return answerDiscount, answerNoise, answerLivingReward

def question3e():
    # Avoid both exits and the cliff (so an episode should never terminate)
    answerDiscount = 0.9   # Doesn't matter much since we're avoiding termination
    answerNoise = 0.2      # Doesn't matter much
    answerLivingReward = 1.0  # High living reward makes agent want to stay alive forever
    return answerDiscount, answerNoise, answerLivingReward

def question8():
    answerEpsilon = None
    answerLearningRate = None
    return answerEpsilon, answerLearningRate
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
