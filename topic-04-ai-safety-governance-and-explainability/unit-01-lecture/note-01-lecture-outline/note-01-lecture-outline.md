---
order: 3
---

# Lecture Outline

Phase I - LO5, LO3

Topic Highlights

## Roadmap

1. **Safety**: the gap between what you asked for and what the model did
2. **Governance**: who answers for the decision, and how they prove it
3. **Documentation**: the artefacts that turn a black box into something you can oversee
4. **Explainability**: four ways to ask "why", and when each one lies to you
5. **The lab**: explain a model, break it on purpose, then write down what you cannot fix

The through-line is last week's credit model, brought back to be explained,
stressed, and given the paperwork that lets someone challenge it.

## What you should be able to do afterwards

- **Classify** a failure by its mechanism, so "the model is broken" becomes
  "the label is a proxy the model is gaming": specification gaming, reward
  hacking, brittleness, or silent failure under distribution shift.
- Explain why a safety failure is not a bug: the model runs as specified,
  returns a clean answer, and harms someone anyway, for reasons the tests
  never sampled.
- **Situate** a model against GDPR Article 22 and the EU AI Act risk tiers,
  and say precisely what that placement obliges you to do. Creditworthiness
  sits in Annex III, so "high-risk" is a to-do list carried before deployment.
- Borrow structure from the NIST AI RMF (govern, map, measure, manage) without
  mistaking a voluntary framework for a law you must obey.
- **Interrogate** an explanation (permutation importance, LIME, SHAP) and
  locate the point where it stops being trustworthy: instability, correlated
  features, plausibility bias, surrogate infidelity, and the alibi.
- **Author** a model card an honest regulator would accept, with metrics
  disaggregated by group and caveats that name what breaks it.
- **Judge** whether an explanation earns trust or merely performs it. An
  explanation makes a model interrogable, not trustworthy.

## Where this goes

Week 3 asked *for whom* the model is wrong. This week asks *how* it fails,
*who* answers for it, and *why* it decides as it does. The disaggregated
metrics in a model card are Week 3's fairness audit reappearing inside this
week's paperwork.

The lecture and the booklet work through a synthetic credit model built so
that income leaks the protected group, which makes the "faithful but unjust
explanation" loud. The lab turns the same questions on the **real** Week 2
classifier, where the story is different: `SEX` turns out to be a top-three
SHAP driver in plain sight, but is barely recoverable from the other features.
As in Week 3, that contrast is the point: you do not know until you measure.

**Week 5** asks whether a protected attribute really disappears when you drop
it, and tests that properly with PCA and clustering. The explanation,
robustness and governance work you do this week is reused on the assigned
dataset in Mini-Deliverable 1A part 3 and Elective 3.

## In the lab

**Safety, Governance and Explainability**: the Week 2 logistic-regression
default model on the UCI credit data, rebuilt with `SEX` in its inputs and
taken through one honest pipeline. Permutation importance and SHAP for the
global picture, LIME on a missed defaulter and then attacked for stability and
for a hidden proxy, a simulated downturn that leaves the approval rate frozen
while the approved book rots, a placement against GDPR and the EU AI Act, and
a governance note, model card and datasheet written from the numbers measured.
One model all the way through; there is no second model or dataset to bring.
