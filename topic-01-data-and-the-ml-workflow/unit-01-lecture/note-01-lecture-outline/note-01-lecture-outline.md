---
order: 3
icon:
  type: fluent:notepad-24-filled
  color: "#2D7FF9"
---

# Lecture Outline

Phase I - LO2, LO5 

Topic Highlights

## Roadmap

1. **The end-to-end ML workflow**
2. **Data types and encoding**
3. **Summary statistics**
4. **Distributions and visualisation**
5. **Correlation — and its traps**
6. **Data processing**
7. **Leakage-safe pipelines**
8. **Governance, documentation & the lab**

## What you should be able to do afterwards

- Place any piece of work in this module at a stage of the ML workflow, and say
  what the previous stage owed it.
- Classify a column as continuous, discrete, categorical, ordinal or binary,
  and choose the encoding that follows from that.
- Report centre, spread and shape for a column, and say when the mean is the
  wrong answer.
- Read Pearson against Spearman, and explain what a single coefficient hides.
- Diagnose a missingness mechanism, including missingness disguised as a valid
  value.
- Build a `ColumnTransformer` and `Pipeline` that cannot leak, and demonstrate
  the leak that occurs without one.
- Write a data dictionary and a datasheet, and say why that is an ethics task
  rather than an administrative one.

## Where this goes

The workflow introduced here is the spine of the module. The profiling you do
this week is what makes Week 2's modelling honest, and the dataset you document
this week is the one Week 3 audits for fairness.

Data governance appears here rather than later on purpose: a datasheet written
before modelling is a description, and one written afterwards is a
justification.

## In the lab

**Know Your Data** — a full profile of the UCI *Default of Credit Card Clients*
dataset, a leakage-safe preprocessing pipeline, and the data dictionary and
datasheet that Weeks 2 and 3 build on.
