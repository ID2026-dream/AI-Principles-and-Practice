---
order: 3
icon:
  type: fluent:notepad-24-filled
  color: "#2D7FF9"
---

# Lecture Outline

Phase I - LO2, LO3

Topic Highlights

## Roadmap

1. **The supervised setup**
2. **Regression**
3. **Classification**
4. **Loss and the bias–variance trade-off**
5. **Evaluation that doesn't flatter**
6. **Framing real problems**

## What you should be able to do afterwards

- Say what a supervised model is, and why generalisation, not fitting the
  training data, is the goal.
- Explain what the train, validation and test sets are each for, and why the
  test set is spent once.
- Frame a question as regression or classification, and treat the choice of
  target as a modelling decision.
- Fit linear, polynomial and regularised (ridge, lasso) regression, and read a
  residual plot as well as an R².
- Describe how logistic regression, k-NN, decision trees, ensembles and support
  vector machines each draw a boundary, and what each one's capacity dial is.
- Diagnose over- and underfitting from a learning curve, and say what to change.
- Cross-validate a whole pipeline, and explain why a single split is an
  anecdote.
- Judge which metric a problem demands (RMSE, MAE, R², precision, recall, F1,
  ROC-AUC, PR-AUC), and show where accuracy misleads.
- Treat the decision threshold as a business decision, set where the costs of
  the two errors balance.

## Where this goes

Week 1 asked what the data is; this week asks what it can decide, and how you
would know if the answer were wrong. The leakage-safe pipeline from Week 1 is
the first step of every model here.

The default classifier you build in the lab is the one **Week 3** audits for
fairness across `SEX`, using the confusion-matrix metrics introduced this week.

## In the lab

**Supervised Learning in Practice**: the same UCI *Default of Credit Card
Clients* data as Week 1, framed two ways (credit limit as regression, default
as classification). A leakage-safe pipeline, a roster of classifiers, learning
and validation curves, cross-validation, the accuracy trap, and a decision
threshold tuned to the cost of each mistake.
