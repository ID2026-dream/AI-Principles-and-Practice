---
order: 3
icon:
  type: fluent:document-text-24-filled
  color: "#176b78"
---


# The Report: Outline and Templates

What goes in your report, section by section, and the LaTeX and Word templates to write it in.

[[toc]]

## The report is your submission

Your report (D1) carries 90% of the project mark. It contains all your results, the links to every
other deliverable at the commit tagged `final`, and the details of how you produced them. Write it
in **LaTeX or Word**, from the course template: both templates have exactly the outline below,
with the tables and appendices already in place. Download them from **Report Templates**, or use
the copies in `report/` in the project starter.

**Length:** about 5,000 words (between 4,000 and 6,000), not counting the title page, abstract, references and appendices.

**Submit:** the PDF on Moodle, and the PDF with its source in `report/` at the commit tagged
`final`, by 23:59 on Wednesday 6 January 2027.

## The outline

### Title page and abstract

- Your project title
- Your name and student number
- Your elective (E1 to E6)
- The link to your repository and the commit tagged final
- The word count of the main body

**Abstract** (150 to 200 words): The question, the data, your approach, your headline result on held-out data, and your main limitation, in one paragraph. *Marked under M6 (Clarity, structure and completeness of the report).*

### 1. Introduction

*About 400 to 600 words · marked under M1 (Question, data and approach)*

- The question your project answers, in one sentence.
- Who would use the answer, and the decision it would help them make.
- Why the question matters, and what makes it hard.
- What you built: a short list of your contributions.
- How the rest of the report is organised.

### 2. Data

*About 600 to 900 words · marked under M1 (Question, data and approach), M2 (Results, reproducibility and correctness)*

- Where the data comes from: your assigned dataset, or (E5 and E6) your personal variant and the simulator or solver you wrote.
- What one example looks like, and a summary table: size, features, missing values, balance of outcomes.
- What you found when you profiled it, and what you did about it.
- How you split (or generated) the data, and how you prevented leakage from test to training data.
- A link to your datasheet or data description.

### 3. Methods

*About 800 to 1,100 words · marked under M1 (Question, data and approach), M3 (From-scratch components and their tests)*

- Your baseline, and why it is a fair comparison.
- Your main model, and why it suits the problem.
- The training set-up: loss, optimiser, step size, batch size, epochs and random seeds.
- How you chose the hyperparameters, and the measure (and any threshold) you use to judge success.
- Your from-scratch components: what you wrote, where the project uses them, and how each is tested (a table: component, file, test, tolerance, result).

### 4. Results

*About 900 to 1,300 words · marked under M2 (Results, reproducibility and correctness)*

- A headline table: baseline against main model on held-out data, with the spread across seeds or folds.
- The loss and metric curves, read for over- and underfitting.
- An error analysis: where the model is wrong, and why.
- Your experiments, one change at a time, and what each one showed.
- For every number: the file in outputs/ that holds it, at the commit tagged final.

### 5. Responsibility

*About 700 to 1,000 words · marked under M4 (Ethics, fairness and explainability audit)*

- The audit: the groups of people (E1 to E4), or the operating regimes or regions of the problem (E5 and E6), and a table of the measured metrics.
- The one mitigation you applied, its measured cost, and who bears that cost.
- The explanations (SHAP, LIME, learned parameters or residual maps), what they show, and where they should not be trusted.
- A summary of your model card and governance note, with links: personal data and GDPR, the EU AI Act risk tier, human oversight.

### 6. Discussion

*About 400 to 700 words · marked under M1 (Question, data and approach), M2 (Results, reproducibility and correctness), M4 (Ethics, fairness and explainability audit)*

- What your results mean for the question and for the person who would use the answer.
- Limitations, and threats to the validity of your results.
- Dead ends from your logbook, and what they taught you.
- What you would do next, with more time or more data.

### 7. Conclusion

*About 150 to 250 words · marked under M6 (Clarity, structure and completeness of the report)*

- The answer to your question in a few sentences, with its main caveat.

### References and appendices

- **References.** Every source you used, in one consistent style (for example IEEE or Harvard), cited in the text. *(M6 (Clarity, structure and completeness of the report))*
- **Appendix A · Deliverables and links.** A table of D1 to D9: for each deliverable, the link to it in your repository at the commit tagged final, and one line on what it contains. *(M6 (Clarity, structure and completeness of the report))*
- **Appendix B · Reproducibility.** Python and package versions, hardware, the exact commands, random seeds, run times, and where the data must be placed (it is never committed). *(M2 (Results, reproducibility and correctness))*
- **Appendix C · From-scratch test results.** The output of python -m pytest -q from a fresh clone, and a sentence on each tolerance. *(M3 (From-scratch components and their tests))*
- **Appendix D · Use of AI tools.** A summary of the AI-use table in your logbook: tool, what you asked, what you used, what you changed or checked; then your declaration. *(M5 (Process evidence: repository history, logbook and AI use))*
- **Appendix E · Changes from your proposal.** What changed since your approved proposal, why, and the logbook entries that record it. *(M5 (Process evidence: repository history, logbook and AI use))*

## Writing it well

- **Every number has a home.** Each result in the report names the file in `outputs/` that holds it, so a reader can check it.
- **Figures earn their place.** Label every axis, caption every figure and table, and say in the text what the reader should see.
- **Write as you go.** Draft each section when you finish that part of the work, not in the last week.
- **Your own words.** The interview asks about what you wrote; record any use of AI tools in Appendix D and your logbook.
