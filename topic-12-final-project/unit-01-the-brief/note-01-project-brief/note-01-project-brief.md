---
order: 1
icon:
  type: fluent:clipboard-task-24-filled
  color: "#a8710b"
---


# The Capstone Project Brief

What you will do, what you hand in, and how it is marked.

[[toc]]

## What you will do

This is the module's capstone project, worth 40% of the module. You will take a dataset you
have never seen, and that general-purpose AI assistants have never seen, through a complete
project: understand the data, build and train a model, write the core of the learning machinery
yourself, audit what you built, and write it all up in a **detailed report** that contains every
result, the links to every other deliverable, and the details of how you produced them. The report
is submitted by 6 January 2027 and carries 90% of the marks; a 10-minute in-person interview in the
week of 11 January 2027 carries the other 10%. Write the report in LaTeX or Word, from the course
template (see **The Report: Outline and Templates**).

You work in one of **six electives**. Each is a different route through the same brief, with the
same deliverables and the same marking. Choose yours this week, in Week 8, and submit the
[Capstone Proposal Form](https://forms.office.com/) by 23:59 on Friday 6 November 2026: your answers are turned into your proposal and your
week-by-week implementation plan, returned to you in Week 9 with your data.

## Key dates

| When | What |
|---|---|
| Week 8 · by 23:59 Friday 6 November 2026 | [Capstone Proposal Form](https://forms.office.com/) submitted |
| Week 9 · Monday 9 November 2026 | Proposal returned; data released for E1 to E4, personal variants for E5 and E6 |
| Weeks 9 to 12 and the break | Build, following the implementation plan in your proposal |
| 23:59 Wednesday 6 January 2027 | Submission deadline: report PDF on Moodle, and the commit tagged `final` pushed |
| Week of 11 January 2027 | 10-minute in-person interview with both lecturers |

## What you hand in

| | Deliverable | What it must contain |
|---|---|---|
| D1 | Report | A detailed report, written in LaTeX or Word from the course template and submitted as a PDF: all your results, the links to every other deliverable, and the details of how you produced them. |
| D2 | Repository | Your code, with a commit history from early in the project and a README that reproduces your results from a clean clone with one command. |
| D3 | Logbook | Decisions, experiments, dead ends and fixes, written as you go, including how you used AI tools. |
| D4 | Trained model | A model trained on your assigned data, with real loss and metric curves. |
| D5 | From-scratch components | Backpropagation, an optimiser step and PCA via SVD written by you, each tested against a reference implementation. |
| D6 | Ethics and fairness audit | Measured group metrics, one mitigation and its measured cost (in E5 and E6, reliability across regimes or across the domain). |
| D7 | Explainability summary | What drives your model's decisions (SHAP or LIME; in E5 and E6, learned physical parameters or residual maps). |
| D8 | Model card and governance note | What the model is for, how it performs for whom, its limits, and the rules that apply to it. |
| D9 | In-person interview | Ten minutes with both lecturers in the week of 11 January 2027: show one key result running from your repository, then answer questions on your report, code, audit and logbook. |

## How it is marked

Six criteria are marked from your report (90% together) and one from the interview (10%). Each is
marked out of 100; your project mark is the weighted sum, and it counts 40% of the module.

| | Element | Weight |
|---|---|---|
| M1 | Report: question, data and approach | 15% |
| M2 | Report: results, reproducibility and correctness | 25% |
| M3 | Report: from-scratch components and their tests | 15% |
| M4 | Report: ethics, fairness and explainability audit | 15% |
| M5 | Report: process evidence (repository history, logbook, AI use) | 10% |
| M6 | Report: clarity, structure and completeness (links to every deliverable) | 10% |
| M7 | In-person interview | 10% |

### Rubric

| Element | 70–100% | 50–69% | 40–49% | below 40% |
|---|---|---|---|---|
| M1 · Question, data and approach | A precise question with a named user; the data understood, its problems found and handled; baseline and main model justified from the problem. | Clear question; data described and prepared sensibly; choices justified in general terms. | Question vague or data handling thin; choices stated rather than justified. | No clear question, or data and methods not described. |
| M2 · Results, reproducibility and correctness | Every number in the report reproduces from a clean clone with one command; leak-free evaluation on held-out data with spread across seeds; results read critically. | Results reproduce with minor intervention; sound evaluation; mostly interpreted. | Results reproduce only with significant help, or some numbers do not match the code. | Results missing, invalid or not reproducible. |
| M3 · From-scratch components | Backpropagation, optimiser step and PCA via SVD correct and used in the project; tests against references pass, with tolerances explained. | All three correct; tests present but partly explained. | Present; tests incomplete or partly failing. | Missing or incorrect. |
| M4 · Audit | Right metrics on the student's own model; one mitigation with its measured cost and who bears it; explanations read with their limits; honest model card and governance note. | Metrics, mitigation and explanations present and mostly interpreted; model card specific to the model. | Metrics computed but not interpreted; no measured cost; generic model card. | Audit or documentation missing. |
| M5 · Process evidence | A real commit history from early on; a logbook written as the work happened, with every AI use recorded; changes from the proposal explained. | Regular history; logbook mostly written as the work happened. | Thin or end-loaded history; logbook written afterwards. | No meaningful history or logbook. |
| M6 · Report quality and completeness | Follows the template; clear, well-structured writing; every figure and table labelled and discussed; every deliverable linked at the final tag; within length. | Well organised and clear; most deliverables linked; minor presentation lapses. | Hard to follow in places; deliverables partly linked; length or structure not respected. | Disorganised or incomplete; deliverables not linked. |
| M7 · In-person interview | Shows a key result running from the repository; explains every component, including the from-scratch code, in their own words; answers "why" and "what if" with evidence. | Shows the result; explains most components and choices; answers most questions with some evidence. | Shows the result only with help; follows the steps but cannot justify choices. | Cannot show or explain central artefacts. |

## The in-person interview

Ten minutes, in person, with both lecturers, in the week of 11 January 2027, worth 10% of the
project mark (M7). You show one key result running from your repository, then answer questions on
your report, code, audit and logbook, including the questions listed in your elective's brief and
in your proposal. Bring the laptop you ran your experiments on, or have your Colab notebook ready.

## Using AI tools

- You may use AI tools to help you, as a helper and not a replacement.
- Record every use in the table in your `LOGBOOK.md`: what you asked, what you used, what you changed.
- You must be able to explain every line you submit; the interview will ask you to, including your from-scratch code.
