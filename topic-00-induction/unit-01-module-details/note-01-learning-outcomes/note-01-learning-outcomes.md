---
order: 2
icon:
  type: fluent:target-arrow-24-filled
  color: "#2D7FF9"
---

# Learning Outcomes

[[toc]]

Five outcomes, each anchored in specific weeks. Nothing here is assessed in the
abstract — every outcome has weeks that teach it and an assessment that tests it.

| LO | Description | Primary weeks |
|---|---|---|
| LO1 | Apply mathematical principles (linear algebra, probability, calculus) | 7, 8, 11 |
| LO2 | Evaluate and distinguish ML paradigms; select appropriate methods | 2, 5, 9 |
| LO3 | Design / implement DL models with industry tools; visualise metrics and limitations | 2, 7, 10, 11 |
| LO4 | Assess structure and learning behaviour of transformer architectures | 10 |
| LO5 | Insight in ethics and safety: fairness, explainability, data governance | 1, 3, 4 |

## How the outcomes are earned

**LO1 — mathematics.** Week 7 derives backpropagation from the chain rule rather
than describing it. Week 8 takes eigendecomposition, SVD and information theory
seriously, and Week 11 uses the calculus again for neural ODEs and diffusion.
The final project asks for backpropagation, an optimiser step and PCA via SVD
implemented from scratch and tested against references, which is the only way
to make this outcome hard to fake.

**LO2 — paradigms and method selection.** Week 2 establishes the supervised
setup, Week 5 removes the labels, and Week 9 asks when to train at all rather
than adapt something pretrained. Selection is assessed by asking you to justify
a choice against a table that includes cost and trainable parameters, not just
accuracy.

**LO3 — implementation and visualisation.** Present from Week 2 onwards and
continuously assessed through the lab portfolio. Every claim about a model has
to be read off a plot you produced.

**LO4 — transformer architectures.** Concentrated in Week 10, where you extract
attention, probe intermediate representations by depth, and run an in-context
learning demonstration. Defended again at the Week 12 viva.

**LO5 — ethics and safety.** Introduced in Week 1 as data governance, made
formal in Week 3 as measurable fairness, and extended in Week 4 into safety,
regulation and explainability. It returns as a required deliverable in the
final project: a measured fairness audit with one mitigation and the measured
cost of that mitigation.
