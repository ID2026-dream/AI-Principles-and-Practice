---
order: 2
icon:
  type: fluent:calendar-ltr-24-filled
  color: "#2d7ff9"
---


# Week by Week: From Proposal to Interview

What to have done by when, whatever your elective.

[[toc]]

## Week 8 · set up and propose

1. Download the **Project Starter**, create a **private** GitHub repository from it, and add both lecturers as collaborators.
2. Run `python -m pytest -q`. Every test fails: that is expected. Your job over the next weeks is to make them pass.
3. Submit the [Capstone Proposal Form](https://forms.office.com/) by 23:59 on Friday 6 November.
4. Graded Lab 8 asks you to write PCA via SVD from scratch: that code becomes `src/scratch/pca_svd.py`.

## Weeks 9 to 11 · build

On Monday 9 November your reviewed proposal comes back, with your data (E1 to E4) or your
personal variant (E5 and E6). Your proposal's implementation plan gives your own version of
this table.

| Elective | Week 9 | Week 10 | Week 11 |
|---|---|---|---|
| E1 | Data explored and prepared; simple models trained, with learning curves. | Your network trained; your three hand-written pieces passing their tests. | Cut-off chosen; percentages checked; fairness check with one fix; SHAP; model card. |
| E2 | Data explored and scaled; readings summed up; PCA via SVD tested. | Number of groups chosen and argued; main PCA directions named. | Autoencoder trained and compared; fairness check with one fix; each group explained. |
| E3 | Simple baseline trained; route chosen; for Route B, the environment working with random actions. | Transformer adapted, or agent learning; hand-written pieces passing their tests. | Attention and layer tests, or reward curves against simple strategies; fairness check with one fix; model card. |
| E4 | Baseline trained; photo and text numbers extracted; PCA tested. | The three adaptation methods compared, with their costs side by side. | Extra-photos experiment; fairness check across areas with one fix; SHAP; model card and governance note. |
| E5 | Your version received; simulator written and checked; clean and noisy data created. | Ordinary and physics-informed models trained and compared; hand-written pieces passing their tests. | Unknown setting found, with how sure you are; reliability check; PCA via SVD. |
| E6 | Your version received; classical solver written and checked; first PINN trained. | Experiments, one change at a time; hand-written pieces, including the input derivative, passing their tests. | Error maps, reliability check, PCA via SVD, time comparison. |

Every week, whatever your elective:

- **Commit as you go**, with messages that say what changed and why. A history that starts in Week 11 costs marks (M5).
- **Write a logbook entry** whenever you decide, experiment, get stuck or fix something.
- **Keep `python reproduce.py` working** from a clean clone. Do not let it rot until January.
- **By the end of Week 10**, decide whether you need the fallback in your proposal, and say so in your logbook.

Graded Lab 10 is due in Week 10 as usual: plan around it.

## Week 12 to 6 January · finish and submit

1. Finish what your plan lists for this period, and complete your logbook, model card and governance note.
2. Write your **report** from the template in `report/` (LaTeX or Word): every result, and a link to every deliverable at the commit tagged `final`.
3. Check from a **fresh clone**: `pip install -r requirements.txt`, `python -m pytest -q` and `python reproduce.py` all work, and reproduce every number in the report.
4. By **23:59 on Wednesday 6 January 2027**: upload the report PDF to Moodle, put the PDF and its source in `report/`, and push the tag: `git tag final && git push origin final`.

## Week of 11 January · the interview

Book an interview slot when the slots are published, and come with the laptop you ran your
experiments on (or your Colab notebook). Ten minutes: you show one key result running from your
repository, then answer questions.
