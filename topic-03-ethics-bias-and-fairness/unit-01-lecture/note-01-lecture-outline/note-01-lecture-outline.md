---
order: 3
icon:
  type: fluent:notepad-24-filled
  color: "#2D7FF9"
---

# Lecture Outline

Phase I - LO5, LO3

Topic Highlights

## Roadmap

1. **Foundations**: why fairness is a modelling decision, not a postscript
2. **Where bias lives**: data, algorithm, society, and the joins between them
3. **Fairness, made precise**: parity, odds, impact, calibration
4. **The catch**: why you can't have every fairness at once
5. **The lab**: audit a real model, break it open, cost the fix

The through-line is one credit model, followed from its base rates all the way
to the price of "fixing" it.

## What you should be able to do afterwards

- **Locate** where bias enters a pipeline you are handed (sampling, historical,
  measurement, labelling, objective, feedback), and argue which entry point
  matters most for a given use.
- Explain why "just maximise accuracy" is already a value choice, and why a
  proxy label is usually where the bias hides.
- Show why deleting the sensitive column ("fairness through unawareness") is
  not a defence on its own, and test for redundant encoding rather than assume
  it away.
- **Judge** a model against several fairness criteria at once (demographic
  parity, disparate impact and the four-fifths rule, equalised odds, equal
  opportunity, calibration), all computed from one confusion matrix per group.
- **Reason** about why those criteria collide: when base rates differ, equal
  calibration and equal error rates cannot all hold (Kleinberg et al. 2016;
  Chouldechova 2017).
- **Cost** a mitigation honestly, at the pre-, in- or post-processing stage:
  what it buys, what it spends, and who ends up paying.
- **Compose** a one-page ethical-impact assessment that a sceptical
  stakeholder would actually accept.

## Where this goes

Week 2 asked what a model can decide and how you would know if it were wrong.
This week asks *for whom* it is wrong. The per-group confusion matrix is just
Week 2's confusion matrix, computed once per group and compared.

The lecture works through a synthetic credit model with a large base-rate gap,
so every effect is loud. The lab then turns the same audit on the **real**
Week 2 classifier, where several of those effects turn out much smaller or
absent. That contrast is the point: you do not know until you measure.

**Week 4** turns from *whether* the model is fair to *why* it decides as it
does, with post-hoc explainability. The audit code you write this week is
reused on the assigned dataset in Mini-Deliverable 1A and Elective 1.

## In the lab

**Auditing a Model for Bias**: the Week 2 logistic-regression default model on
the UCI credit data, retrained without `SEX` and put on trial across it.
Per-group confusion matrices and `MetricFrame`, the four-fifths rule and why
it is an operating-point property, equalised odds and calibration by group, a
probe for whether dropping the column actually removed it, the impossibility
result reproduced with `ThresholdOptimizer`, and a mitigation costed in
declined applications rather than accuracy.
