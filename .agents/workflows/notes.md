---
description: Generate comprehensive session notes after completing a learning module or feature.
---

# Generate Session Notes

The developer wants to solidify their learning by generating a permanent set of notes for the topic they just studied.

Create or update a markdown file in the relevant project directory (e.g., `TopicName_Notes.md`).

The notes must be highly detailed, educational, and use plain English (avoid LaTeX/math rendering that doesn't display well in plain text UI). 

Follow this exact structure when generating the notes:

## 1. Full Workflow Algorithm with Explanations
Explain the core algorithm or concept step-by-step.
For every step, explicitly include:
- **What:** What is happening in this step mathematically or programmatically.
- **Why:** Why this step is necessary for the overall goal.

## 2. Key Terminology
Define any new or important jargon used during the session (e.g., Independent vs. Dependent variables, Hyperparameters, etc.).

## 3. Deep Dives
Take 1 or 2 of the most complex concepts from the session and explain them in detail (e.g., Learning Rate, Cost Functions, etc.). 
Explain what happens when things go wrong (e.g., what if the learning rate is too high?).

## 4. Real-World Application
Explain how this concept or algorithm is used in the real world outside of a toy example.
Include practical steps (e.g., importing real datasets with pandas, scaling data).

## 5. Pseudocode
Provide a clear, language-agnostic pseudocode block for the algorithm so the logic is easy to read without language-specific syntax clutter.

## 6. Dry Run Simulation
Provide a step-by-step manual simulation of the algorithm running for a single iteration or a small set of data.
Show the exact math and how the variables change state. This is crucial for verifying understanding.
