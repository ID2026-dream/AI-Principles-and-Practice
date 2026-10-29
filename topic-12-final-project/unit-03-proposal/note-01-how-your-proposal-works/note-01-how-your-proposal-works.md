---
order: 2
icon:
  type: fluent:notepad-24-filled
---


# How Your Proposal Works

You answer a short form; your answers become your proposal and your implementation plan.

[[toc]]

## The three steps

1. **Draft your answers.** All the questions are listed below, so you can think and write before you open the form.
2. **Submit the [Capstone Proposal Form](https://forms.office.com/)** by 23:59 on Friday 6 November 2026 (end of Week 8). To change an answer, submit the form again before the deadline: your most recent response is the one used.
3. **Receive your proposal.** On Monday 9 November (Week 9) the lecturers turn your answers into `PROPOSAL.md`: your question and who it is for, your data and measure of success, your approach and from-scratch plan, your responsibility plan next to what your elective requires, your week-by-week implementation plan, the deliverables, and the questions to prepare for the interview. It comes back marked *approved*, *approved with changes*, or *resubmit*, and your data (or personal variant) is released with it.

Put `PROPOSAL.md` in your repository (the project starter has a place for it) and keep it up to date: if your plan changes, edit it and record why in your logbook.

## What makes a good answer

- **Specific.** "Recall across age bands, because a missed patient is the costly error" beats "I will check fairness".
- **Short.** Two or three sentences per question are enough.
- **Yours.** The interview asks about these decisions; write what you actually intend to do.

## Your implementation plan is checked

Questions 18 to 21 ask what you will have done by the end of Weeks 9, 10 and 11, and what you will
finish between Week 12 and the 6 January deadline. Your proposal turns them into your implementation
plan, and checks that, between them, they include every part the project needs:

- data prepared, split or generated
- baseline trained (or, in E6, the reference solver built)
- main model trained, with loss and metric curves
- from-scratch components passing their tests
- fairness or reliability audit, with one mitigation
- explanations of what drives the model
- model card and governance note

Anything missing is listed in your proposal under **Gaps to close**, so that you can add it to a
week before you start.

## The questions

Everyone answers the same 26 questions, whatever their elective. Open the [Capstone Proposal Form](https://forms.office.com/) when you are ready.

### About you

1. Your full name
2. Your student number
3. The link to your private project repository (add both lecturers as collaborators)
4. Which elective will you take?

### Your project

5. A short working title for your project
6. In one sentence, what question will your project answer?
7. Who would use your answer, and what decision would it help them make?
8. What data will your model learn from (your assigned dataset, or the data you will generate from your equations), and what does one example look like?
9. What exactly will your model output, and which measure will tell you whether it is good enough?

### Your approach

10. What is your simple baseline, and why is it a fair comparison?
11. What is your main model, and why does it suit this problem?
12. How will you split (or generate) your data so that your evaluation is honest, with nothing leaking from the test data into training?
13. Where will your own backpropagation, optimiser step and PCA via SVD be used in your project, and how will you test each one?

### Responsibility

14. Who or what could your model treat unequally (groups of people; or, in E5 and E6, operating conditions or regions of the problem), and what will you measure to find out?
15. What one fix will you try if you find a gap, and how will you measure what it costs?
16. How will you show what drives your model's decisions?
17. Which rules and risks apply to your project (for example personal data, GDPR, the EU AI Act, safety), and how will you handle them?

### Your implementation plan

18. What will you have done by the end of Week 9?
19. What will you have done by the end of Week 10?
20. What will you have done by the end of Week 11?
21. What will you finish between Week 12 and the submission deadline on 6 January 2027, including your report?
22. What is the riskiest part of your plan, and what will you do instead if it is not working by the end of Week 10?
23. Where will you run your experiments? *(choose one: My own laptop, CPU only; My own laptop with a GPU; Google Colab; The lab workstation)*
24. How do you plan to use AI tools in this project, and how will you record that use?
25. Which part of the project would you most like help with? *(choose one: Preparing the data; Building and training the models; The from-scratch components; The fairness check, explanations and documentation; Planning my time)*
26. Declaration
