# Activity 7 Reflection Answers

## Checkpoint 1 — Visualizing Boundaries
Chunk 0 is `[0, 100]`, chunk 1 is `[80, 180]`, chunk 2 is `[160, 200]` — each new chunk starts at `end - overlap`, so it backs up 20 characters from where the last one ended.

---

## Q1 — Which strategy won?
Fixed-size technically won the query, but the returned text starts mid-word and cuts off mid-sentence — it only scored higher because it accidentally bled across two paragraphs and matched more vocab words. Paragraph chunking would've returned a cleaner, complete sentence but lost the vector race.

---

## Q2 — Fixed Chunk #2 vs Paragraph Chunk #2
Fixed chunk #2 is a Frankenstein piece that starts as a leftover fragment and ends mid-word (`"when a sent"`), while paragraph chunk #2 is two clean complete sentences on one idea. Fixed-size just counts 140 characters and moves on, it has no idea a sentence boundary even exists.

---

## Q3 — HR Manual problem
If a policy says "Employees get 15 days leave — this excludes probationary staff" and those two sentences land in different fixed-size chunks, the chatbot tells a probationary employee they have 15 days because it never retrieved the disclaimer. Paragraph chunking keeps them together since they live in the same paragraph, which is exactly where the semantic relationship is.

---

## Q4 — Why store metadata?
The retrieved vector is just floating point numbers like `[0.0, 0.7071, 0.0, 0.7071...]` — without the payload you have no idea what document it came from, where in the doc it lives, or how to debug a bad answer. `chunk_index` alone lets you grab neighboring chunks to reconstruct context when the returned piece is clearly cut off.