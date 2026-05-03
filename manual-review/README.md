# manual-review/

Line-numbered copies of the raw OCR text for scrolling + locating boundary line numbers by eye. Used in tandem with `MANUAL-REVIEW.md` at repo root and `tools/manual-fill.py`.

## Files

- `pt1-numbered.txt` — Vol I pt 1 (d.1–23), line-numbered copy of `raw/bonaventure_vol1_raw.txt`
- `pt2-numbered.txt` — Vol I pt 2 (d.24–48), line-numbered copy of `raw/bonaventure_vol1_pt2_raw.txt`

Both are gitignored (same policy as `raw/*_raw.txt`). Line numbers are 6-char right-aligned followed by two spaces.

## Regenerate

```bash
awk '{printf "%6d  %s\n", NR, $0}' raw/bonaventure_vol1_raw.txt     > manual-review/pt1-numbered.txt
awk '{printf "%6d  %s\n", NR, $0}' raw/bonaventure_vol1_pt2_raw.txt > manual-review/pt2-numbered.txt
```

## Typical use

1. Open the numbered file in an editor. Search for the distinction's heading (e.g. `DISTINCTIO XXX`).
2. Scroll to where the Divisio textus or missing chunk should begin.
3. Copy the start + end line numbers into `MANUAL-REVIEW.md`'s slots.
4. Run `python3.11 tools/manual-fill.py --part N --dist N --type TYPE --lines START-END` to write the skeleton.
5. Re-run `python3.11 tools/boundary-audit.py --part N` to confirm the issue cleared.

## Handy grep

```bash
# d.N area in pt2 (e.g. d.30):
grep -n "DISTINCTIO XXX\b" manual-review/pt2-numbered.txt
# sub-markers within a range (replace 10160 10400 with your bounds):
awk 'NR>=10160 && NR<=10400' manual-review/pt2-numbered.txt | grep -E "QUAESTIO|ARTI|DIVISIO|DUB|COMM"
```
