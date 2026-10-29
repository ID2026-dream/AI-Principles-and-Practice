---
order: 3
icon:
  type: fluent:presenter-24-filled
  color: "#a8710b"
---


# Submission and Interview

How to submit, what the interview looks like, and a final checklist.

## Submitting

By **23:59 on Wednesday 6 January 2027**:

1. **Upload your report as a PDF to Moodle.** This is your submission, and 90% of the project mark.
2. **Push the commit tagged `final`**, with the same PDF and its LaTeX or Word source in `report/`. The links in your report point to this commit.

Also check that:

- both lecturers are collaborators on the repository (from Week 8);
- the data is **not** in the repository: `data/` is git-ignored in the project starter.

## The interview

Ten minutes, in person, with both lecturers, in the week of 11 January 2027.

1. **Show one key result** running from your repository: `python reproduce.py`, or a reduced version of it if training takes long.
2. **Answer questions** on your report, code, results, audit and logbook. Expect at least one question on your from-scratch code, and the questions listed in your proposal.

The interview is element M7, worth 10% of the project mark. Both lecturers agree the mark on the day.

## Final checklist

- [ ] The report follows the template, is about 5,000 words, and links every deliverable in Appendix A (D1)
- [ ] `python reproduce.py` reproduces every number in the report from a fresh clone (D2, D4)
- [ ] `python -m pytest -q` passes from a fresh clone (D5)
- [ ] The audit has measured metrics, one mitigation and its measured cost (D6)
- [ ] The explainability summary, `MODEL_CARD.md` and `GOVERNANCE.md` are complete (D7, D8)
- [ ] `PROPOSAL.md` is up to date; every change and every use of AI tools is in `LOGBOOK.md` (D3)
- [ ] The report PDF is on Moodle, and the commit tagged `final` is pushed, by 23:59 on Wednesday 6 January 2027
