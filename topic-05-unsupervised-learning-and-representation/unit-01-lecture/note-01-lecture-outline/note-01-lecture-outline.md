---
order: 3
icon:
  type: fluent:notepad-24-filled
  color: "#2D7FF9"
---

# Lecture Outline

Phase I - LO1, LO2

Topic Highlights

## Roadmap

1. **No labels**: what the problem even is once the answer column is gone
2. **Clustering**: K-means, hierarchical and Gaussian mixtures, three different opinions about what a group is
3. **Choosing K**: a decision you defend, not a number the data hands you
4. **PCA**: your first machine that learns a new set of axes from the data itself
5. **Embeddings**: geometry as meaning, the idea the rest of the course is built on
6. **The lab**: cluster, validate, reduce, then interrogate what the representation leaks

The through-line is the credit data again, this time with the label *and* the
protected group taken away, to see whether the geometry hands the group
straight back.

## What you should be able to do afterwards

- **Contrast** K-means, hierarchical clustering and Gaussian mixtures by the
  assumption each one smuggles in, not by their pseudocode: equal round balls,
  whatever the linkage implies, or tilted ellipses with soft membership.
- Explain why clustering *proposes* structure rather than discovering it. Every
  method returns an answer on any data, including data with no clusters at all,
  so the output is a hypothesis you have to defend.
- **Adjudicate** a disagreement between the elbow and the silhouette, and
  defend the K you settled on in a sentence. Neither chart decides; you do.
- Say what internal validity can and cannot certify. A high silhouette means a
  tidy partition, not a useful one, and not a fair one.
- **Interpret** a principal component in the language of the domain by reading
  its loadings, rather than leaving it as "PC1".
- **Critique** a learned representation for the structure it reproduces without
  being asked, including a protected attribute you dropped.
- **Construct** a 2D map of the credit applicants and argue for what its shape
  means, including what it hides.

## Where this goes

Weeks 2 to 4 built and interrogated models. This week names the thing those
models were quietly standing on the whole time: the representation. From here
on, "what representation is this running on?" is a question you ask by reflex.

The lecture and the booklet work through a synthetic four-feature credit
dataset in which the protected group is entangled with income, history and
debt. There, PC1 alone recovers the group 71% of the time against a 43% base
rate, almost exactly what the supervised score leaked in Week 4. The lab runs
the same probe on the **real** UCI credit data, where `SEX` turns out to be
barely recoverable. Same method, opposite conclusion: recoverability is a
property of the dataset, and you only find out which world you are in by
measuring.

**Week 6** is the quiz and reflection milestone. From **Week 7** the course
moves to neural networks, where representations stop being linear and start
being learned end to end. The clustering, PCA and recovery work you do this
week returns as **Elective 2** of the assignment, run on the dataset you are
assigned, and the recovery result feeds back into the Week 3 fairness work and
the Week 4 governance note.

## In the lab

**Unsupervised Learning and the Idea of a Representation**: the UCI credit data
with both the `default` label and `SEX` removed, taken through four moves.
Cluster with K-means and defend a K from the elbow and the silhouette; meet
hierarchical clustering and a Gaussian mixture; reduce with PCA and name the
axes from their loadings; then bring the label back to ask whether the dominant
structure has anything to do with default, and probe whether `SEX` can be
rebuilt from a representation that never saw it.
