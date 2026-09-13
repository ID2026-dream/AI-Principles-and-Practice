# Week 1 Lab Submission — Know Your Data

AI Principles and Practice · COMP-0987 · Topic 01, Unit 02

One section below for each section of the lab. Answer as you go, rather than
at the end — most of these are the checkpoint questions you have already talked
through at the bench.

Short answers. One or two sentences unless it says otherwise. Delete each
`TODO` as you finish that section, then run `python make_submission.py`.

| | |
|---|---|
| Student number | TODO |
| Name | TODO |
| Date | TODO |

---

## Section 1 — First contact

**1.1 How many rows and columns, and how many literal blanks, does the file
have? Which three columns carry codes that are not in the documentation, and
how many rows does each affect?**

TODO

**1.2 Why is the `PAY_0` finding more serious than the `EDUCATION` one, even
though both are undocumented codes?**

TODO

**1.3 The documented "paid duly" code (−1) defaults at 16.8%; the undocumented
−2 and 0 default at 13.2% and 12.8%. One sentence proposing what −2 and 0 most
likely mean, and a second on how confident you are and why behaviour is weaker
evidence than a codebook.**

TODO

---

## Section 2 — Summary statistics

**2.1 When do the mean and median disagree on this dataset, and which would you
report? Why is the IQR the safer measure of spread here?**

TODO

**2.2 `PAY_AMT1` has a skew of 14.7 and an excess kurtosis of 415. Say what
that means in plain words to someone who has never heard of kurtosis, and name
one modelling consequence.**

TODO

**2.3 You redrew the `PAY_AMT1` histogram on a log scale. What does the
log-scaled version show that the raw one cannot?**

TODO

---

## Section 3 — Correlation

**3.1 One example where Pearson understates a relationship and one where it
overstates it. Give both coefficients.**

TODO

**3.2 Adjacent bill months correlate at about 0.95. Name one problem that
causes for a linear model's coefficients, and one feature you could build from
the six columns that might carry more than any of them alone.**

TODO

**3.3 The strongest correlation with the target in the whole table is 0.325.
Write down a number for how accurate you expect next week's models to be. You
will check this against your Week 2 results.**

TODO

---

## Section 4 — Processing

**4.1 Why did `df.isna().sum()` return zero on a dataset with hundreds of
unknown values?**

TODO

**4.2 Two or three sentences arguing against `df.dropna()` here. Defend the
specific claim: dropping those 399 rows would destroy information *and* bias
what remains.**

TODO

**4.3 The IQR and z-score rules flagged 2,400 and 686 values. Why the gap, and
which do you believe? Then: 590 clients have a negative bill. One sentence on
what that means, and one on why deleting those rows would be a mistake.**

TODO

---

## Section 5 — Augmentation

**5.1 Why must the split come before the resampling, and never the other way
round? What does `stratify=y` protect you from?**

TODO

**5.2 SMOTE raised recall from 0.23 to 0.64, dropped precision from 0.74 to
0.36, and accuracy fell from 0.81 to 0.67. Two sentences on which setting you
would ship to a bank, and what you would need to know to decide.**

TODO

---

## Section 6 — Leakage-safe pipelines

**6.1 What single change turned an F1 of 0.665 into 0.473, and which of the two
is the truth?**

TODO

**6.2 Name the four preparation steps inside your `ColumnTransformer` and say
what each one learns from the training data. Why is a pipeline a structural fix
rather than a stylistic preference?**

TODO

**6.3 Does your pipeline run end to end? Give the accuracy you got, and say how
it compares with predicting "no default" for everyone.**

TODO

---

## Section 7 — Governance and documentation

### 7.1 Data dictionary

All 25 columns. The Notes column should carry something you could only know by
having done Sections 1–4, not a restatement of the column name. Paste your
completed table here, or say which file in your submission holds it.

| Column | Type | Allowed values | Notes for a future user |
|---|---|---|---|
| `ID` | identifier | 1–30000 | Row identifier, not a feature. Drop before modelling. |
| TODO | | | |

### 7.2 Datasheet

A paragraph each, following Gebru et al. (2021).

**Why does it exist, and who made it? Who is represented, and who is excluded?**

TODO

**How was it collected and with what consent, and what was done to it before
you got it?**

TODO

**What may it be used for, and name one use that would be inappropriate.**

TODO

**Known biases and limitations. Men default at 24.2% and women at 20.8% before
any model exists — include that, and say why documenting it is a governance
task rather than a modelling one.**

TODO

---

## Section 8 — Exercises

8.1 is Section 7 above, so it is already done. Attempt 8.2 and 8.3, then do
*either* 8.4 *or* 8.5 — not both.

**8.2 Do the `-2` and `0` codes behave the same as each other? Two sentences
either way, with the evidence you used.**

TODO

**8.3 Your feature from the six bill columns, its correlation with the target,
and whether it beat `PAY_0`'s 0.325. If it did not, say whether you would keep
it anyway.**

TODO

**8.4 or 8.5 — say which one you did, then answer it.**

TODO

---

## Before you build the zip

**Use of AI assistants.** Say what you used one for, if anything, and what you
checked yourself. Using one is allowed; not being able to explain your own
submission is the problem. "None" is a complete answer.

TODO

**Anything you want to flag.** Optional — if something went wrong, if you ran
out of time, or if you want a second opinion on a judgement call. Delete the
TODO either way.

TODO
