# AI Principles and Practice — Tutors course source

COMP-0987 · Level 9 (Postgraduate) · 10 Credits
Department of Computing and Mathematics, SETU

This folder is the **source** for a [Tutors](https://tutors.dev) course. It is a
tree of markdown files and assets named according to the conventions in the
[Tutors reference manual](https://tutors.dev/course/tutors-reference-manual).
The build step turns it into a `json/` folder, which is what gets deployed.

---

## Build and publish

Install [Deno](https://deno.com/), then from this folder:

```bash
deno run -A jsr:@tutors/tutors
```

That writes a `json/` folder. Drag it onto [Netlify Drop](https://app.netlify.com/drop/)
and the course is live.

For a local, offline copy without the Tutors reader:

```bash
deno run -A jsr:@tutors/tutors-lite     # writes html/ — open html/index.html
```

### Continuous deployment

Push this folder to GitHub, import the repo into Netlify, and set:

| Setting | Value |
|---|---|
| Build command | `deno run -A jsr:@tutors/tutors` |
| Publish directory | `json` |

Every push then rebuilds the course.

### Check before you build

```bash
python3 validate.py
```

Catches the mistakes that produce a course which builds but renders wrong — a
talk whose PDF name does not match its markdown, a `web-*` folder with no
`weburl`, a unit with no title file, a space in a folder name.

---

## Structure

```
.
├── course.md            course title and blurb          (mandatory)
├── properties.yaml      credits, icon, auth, llm         (mandatory)
├── calendar.yaml        semester schedule + assessments
├── enrollment.yaml      educators and students (needs auth: 1)
├── validate.py          convention checker
│
├── topic-00-induction/          Week 0 — module descriptor, semester map, setup
├── topic-01-…-workflow/         Week 1 — Data Analysis and the ML Workflow
├── topic-02-supervised-learning/
├── …
├── topic-06-quiz-and-reflection/   milestone — no new teaching content
├── …
└── topic-12-final-project/         milestone — the capstone brief
```

Every teaching week has the same shape:

```
topic-NN-slug/
├── topic.md                        title, summary, icon
├── unit-01-lecture/
│   ├── unit.md
│   ├── talk-01-slug/               ← the slide deck
│   │   ├── talk-01-slug.md         card title + summary
│   │   └── talk-01-slug.pdf        the deck itself
│   └── note-01-lecture-outline/
│       └── note-01-lecture-outline.md
└── unit-02-lab/
    ├── unit.md
    └── book-01-slug/               multi-step lab
        ├── 00.Lab-NN.md            step 0 — its title becomes the lab card title
        ├── 01.Something.md
        └── …
```

Week 1 additionally carries `tutorial-01-reference-booklet/`, the 35-page
portrait booklet. Portrait documents go in as **tutorials**; landscape slide
decks go in as **talks**. Both are PDFs — the folder prefix is what decides how
Tutors renders them.

---

## What is already here

- All 13 topics with titles, summaries and icons.
- Both milestone weeks written out: Week 6 quiz scope and check-in, Week 12
  full project brief across six steps including the marking breakdown.
- The induction topic: the module descriptor PDF, notes on learning outcomes
  and assessment, a five-step semester map, an environment-setup note and four
  reference links.
- Ten lecture outline notes, one per teaching week, carrying the lecture and
  lab bullets straight from the descriptor.
- Ten multi-step labs — 54 steps in total — written from the lab descriptions
  in the descriptor.
- Ten placeholder slide decks, one per teaching week.
- `calendar.yaml` covering Weeks 0–12 with the quiz, assignment and project
  marked as assessments.

## What needs filling in

1. **The slide decks.** Each `talk-01-*/talk-01-*.pdf` is a four-slide
   placeholder carrying that week's outline. Overwrite the PDF, keeping the
   filename exactly as it is. See `AUTHORING.md`.
2. **Calendar dates.** `calendar.yaml` currently starts Week 1 at
   `2026-09-14`. Set the real dates and insert reading weeks with `week: ~`.
3. **Companion links.** Uncomment `moodle`, `teams` or `youtube` in
   `properties.yaml` once the real URLs exist.
4. **Lab archives.** Add a `archive-01-*/` folder per week when there are
   starter files or notebooks to distribute.
5. **Lecture videos.** Add a `panelvideo/` folder to any lecture unit once
   recordings exist. Format in `AUTHORING.md`.
6. **GitHub edit button.** Set `github:` in `properties.yaml` once the repo is
   public, and every page gains an "edit this page" link.

---

## Progressive release

Two mechanisms, both documented in the manual.

**Content locking** (recommended) needs `auth: 1` in `properties.yaml` and an
`enrollment.yaml` listing educator GitHub IDs. Educators then toggle topic
visibility live from the educator panel, with no rebuild.

**`ignore` / `ignorepin`** needs no sign-in. Uncomment the block in
`properties.yaml`, list the topics to hide, and uncomment one per week as you
release it. The PIN reveals hidden topics to staff.

---

## Reference

- Tutors reference manual — <https://tutors.dev/course/tutors-reference-manual>
- LLM-friendly full manual — <https://tutors-reference-manual.netlify.app/llms/tutors-reference-manual-complete-llms.txt>
- Reference course source — <https://github.com/tutors-sdk/tutors-reference-course>
