# Antigravity Learning System Guide

## Discover Northeast 2.0

This folder contains the configuration for the AI-assisted learning system being used to build Discover Northeast 2.0.

The purpose of this system is different from a normal AI coding setup.

The goal is:

> **You build the software. Antigravity guides, teaches, reviews, and helps you recover when stuck.**

The system is intentionally designed to reduce AI dependency over time.

---

# 1. The Basic Philosophy

Normal AI coding workflow:

```text
Idea
 ↓
Ask AI
 ↓
AI writes code
 ↓
Project works
```

Our workflow:

```text
Problem
 ↓
Requirement
 ↓
Understand the concept
 ↓
Plan the solution
 ↓
You implement
 ↓
You get stuck
 ↓
Mentor gives hints
 ↓
You continue
 ↓
Review
 ↓
Next problem
```

The objective is not to finish the project as quickly as possible.

The objective is to become capable of building the project independently.

---

# 2. What Is Inside `.agents/`?

```text
.agents/
│
├── rules/
│   └── mentor.md
│
├── workflows/
│   ├── start.md
│   ├── next.md
│   ├── stuck.md
│   ├── review.md
│   └── daily-review.md
│
└── GUIDE.md
```

There are two important types of configuration here:

### Rules

Rules define how Antigravity should behave.

### Workflows

Workflows define repeatable processes that you can manually trigger.

`GUIDE.md` is simply documentation for you.

---

# 3. `rules/mentor.md`

## What it does

`mentor.md` is the permanent behavioral rule for this project.

It tells Antigravity:

> "You are my mentor, not my replacement."

It establishes the core learning philosophy.

---

## Important behaviors

The mentor should:

- explain concepts
- explain the problem being solved
- break work into tasks
- identify relevant files
- guide implementation
- review your code
- help debug
- track weaknesses
- ask questions that test understanding

The mentor should NOT:

- automatically build features
- rewrite your code unnecessarily
- solve problems immediately
- introduce unnecessary technologies
- optimize for speed over learning

---

## Assistance Levels

When you are stuck, the mentor follows an escalation system.

### Level 1: Question

The mentor asks a question that helps you reason toward the answer.

### Level 2: Hint

The mentor explains the relevant concept.

### Level 3: Pseudocode

The mentor explains the algorithm or logic without real implementation.

### Level 4: Skeleton

The mentor gives incomplete code that you finish.

### Level 5: Example

The mentor demonstrates the concept in a small isolated example.

### Level 6: Implementation

The mentor gives the complete implementation.

This should only happen when you explicitly request it after attempting the problem yourself.

---

# 4. `workflows/`

Workflows are reusable commands for common situations.

You do not need to remember the contents of these files.

You only need to remember the commands.

---

# 5. `/start`

## Purpose

Start or resume a development session.

Use this when:

- beginning the project
- beginning a new day
- returning after being away
- you are unsure what state the project is in

The workflow should inspect the current project state and explain:

- where we are
- what has been completed
- what is currently being built
- what the current objective is

It should then give you the first appropriate task.

Example:

```text
/start
```

---

# 6. `/next`

## Purpose

Find the next thing you should work on.

This is one of the most important commands.

Use it whenever you finish a task and think:

> "Okay, what do I do now?"

The workflow should consider:

- product requirements
- current project state
- completed work
- current architecture
- design
- learning objectives
- unfinished features

It should identify the next meaningful problem.

It should NOT simply give you a random coding task.

The next task should follow the product's development progression.

Example:

```text
/next
```

Possible response:

```text
CURRENT MISSION

Problem:
Users cannot explore destinations by state.

Requirement:
Users should be able to open a state
and see its destinations.

Concept:
Dynamic routes.

Your first task:
Create the state route.

Do not connect the database yet.
```

---

# 7. `/stuck`

## Purpose

This is the emergency button.

Use it when you genuinely do not know how to proceed.

Example:

```text
/stuck
```

The mentor should inspect:

- your current code
- recent changes
- errors
- terminal output
- relevant files
- the task you are working on

Then it should determine what kind of problem you have.

Possible categories:

- conceptual
- syntax
- logic
- architecture
- database
- API/library
- configuration
- debugging

It should then use the assistance ladder.

Remember:

> `/stuck` does NOT mean "fix this."

It means:

> "Help me understand how to get unstuck."

---

# 8. `/review`

## Purpose

Review something you have implemented.

Use this after completing a meaningful task or feature.

Example:

```text
/review
```

The mentor should inspect your implementation and evaluate:

- functionality
- code quality
- architecture
- error handling
- security
- edge cases
- testing
- maintainability
- your understanding

It should not automatically fix problems.

Instead, it should tell you what needs improvement and let you make the changes.

---

# 9. `/daily-review`

## Purpose

Review your learning progress at the end of the day.

Example:

```text
/daily-review
```

The mentor should review:

- today's work
- Git changes
- completed features
- concepts learned
- concepts you struggled with
- recurring mistakes
- AI dependency
- independence

It should then give you:

### What you accomplished

### What you learned

### What remains weak

### What to work on next

### How independently you worked

This is not meant to judge you.

It is meant to make your progress visible.

---

# 10. Your Daily Workflow

Your normal development loop should be:

```text
/start
   ↓
/next
   ↓
Understand the problem
   ↓
Understand the concept
   ↓
Plan
   ↓
You write code
   ↓
Stuck?
   │
   ├── No ───────────────┐
   │                     │
   └── Yes → /stuck      │
                         │
                         ▼
                      Continue
                         │
                         ▼
                      /review
                         │
                         ▼
                       /next
                         │
                         ▼
                    More features
```

At the end of the day:

```text
/daily-review
```

---

# 11. How You Should Talk to the Mentor

Prefer questions like:

```text
I'm stuck here.
```

```text
I don't understand why this works.
```

```text
What concept am I missing?
```

```text
Give me a hint.
```

```text
Give me a stronger hint.
```

```text
Can you give me pseudocode?
```

```text
Can you give me a skeleton?
```

```text
Review what I wrote.
```

Avoid immediately saying:

```text
Build this for me.
```

or:

```text
Fix everything.
```

Those requests bypass the learning process.

---

# 12. The Project Development Philosophy

The project should develop from problems and requirements.

Not from a list of technologies.

Bad learning flow:

```text
Today:
Learn PostgreSQL

Tomorrow:
Learn authentication

Next:
Learn Leaflet
```

Better learning flow:

```text
Users need destination information
        ↓
We need persistent data
        ↓
Learn database fundamentals
        ↓
Create destination data
```

Then:

```text
Users need to explore destinations
        ↓
We need state/destination relationships
        ↓
Learn relational data
        ↓
Implement relationships
```

Then:

```text
Users want to save destinations
        ↓
We need to know who the user is
        ↓
Learn authentication
        ↓
Implement authentication
```

The product drives the learning.

---

# 13. Technology Rules

The initial project stack is intentionally simple.

## Core

- Next.js
- JavaScript
- React
- CSS / CSS Modules

## Backend / Data

- Supabase
- PostgreSQL
- Supabase Auth
- Supabase Storage

## Maps

- Leaflet
- OpenStreetMap

## Deployment

- Vercel

---

# 14. Technologies We Are Deliberately Avoiding

For this project, avoid adding technologies just because they are popular.

Currently avoid:

- TypeScript
- Tailwind
- Redux
- unnecessary state management
- separate Express backend
- MongoDB
- microservices
- unnecessary libraries

This does NOT mean these technologies are bad.

It means:

> **We are limiting the number of things you have to learn simultaneously.**

The goal is depth, not technology collection.

---

# 15. When Can New Technologies Be Added?

A new technology should be introduced when:

1. The product actually needs it.
2. The existing stack cannot reasonably solve the problem.
3. You understand why the new technology is being introduced.
4. The learning value justifies the added complexity.

For example:

TypeScript can be introduced later after you are comfortable with JavaScript and the application architecture.

---

# 16. Git Is Part of the Learning Process

Commit small, meaningful changes.

Examples:

```text
feat: create destination card

feat: add state route

feat: connect destinations to database

feat: display destinations on state page

fix: handle missing destination
```

Do not worry about creating perfect commits.

The purpose is to make your progress and changes easy to inspect.

---

# 17. Design Comes Before Implementation

The application should not be built entirely from imagination while coding.

The intended flow is:

```text
Product idea
 ↓
Requirements
 ↓
User experience
 ↓
Design
 ↓
Implementation
```

Figma/Figma Make can be used to explore the visual design.

The resulting design decisions should eventually be recorded in:

```text
docs/design.md
```

Antigravity should use that document as a design reference when implementing the application.

---

# 18. What Success Means

Success is NOT:

> "The website is finished."

Success is:

> "I understand how the website works and I can reproduce significant parts of it without AI."

Track:

- features completed
- concepts understood
- recurring weaknesses
- AI assistance level
- independent implementation ability

---

# 19. The Long-Term Goal

The first project is not supposed to make you an expert.

It is supposed to prove that you can gradually take ownership of software development.

The progression should eventually look like:

```text
AI writes most code
        ↓
AI guides implementation
        ↓
AI gives hints
        ↓
AI reviews code
        ↓
AI helps with difficult problems
        ↓
You build independently
        ↓
AI becomes a senior engineer beside you
```

The final goal is not to stop using AI.

The goal is:

> **AI becomes an accelerator rather than a dependency.**

---

# 20. Quick Reference

| Command | Use it when |
|---|---|
| `/start` | Start or resume work |
| `/next` | Ask what to build next |
| `/stuck` | You don't know how to proceed |
| `/review` | You finished a task/feature |
| `/daily-review` | End of the day |

If you remember only one thing:

```text
/next
```

means:

> **"What is the next problem I should solve?"**

And:

```text
/stuck
```

means:

> **"Help me solve this without taking over."**

---

# Final Principle

You are not following an AI-generated coding tutorial.

You are building a real application.

The mentor exists to keep you moving through the engineering process while ensuring that you remain the person doing the actual development.

The project should gradually become more complex as your ability increases.

One problem.

One concept.

One task.

One implementation.

One review.

Then the next problem.