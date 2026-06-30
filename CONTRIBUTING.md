# Contributing

This is a vendor-neutral comparison of age verification software providers, scored on methods, coverage, and pricing model rather than a single rating. Corrections and additions are welcome.

## Edit the data, not the table

1. Edit [tools.yaml](tools.yaml). Fields: `name`, `url` (optional), `methods`, `coverage`, `pricing`, `best_for`.
2. Run `python render_table.py --write` to rewrite the table between the `<!-- TABLE:START -->` and `<!-- TABLE:END -->` markers.
3. Open a PR with a source link for any method, coverage, or pricing claim.

## What gets merged

- Claims backed by the vendor's own page or documentation. Pricing especially, since it moves.
- Pricing model stated precisely: per attempt, per completed check, or per approval. These are not interchangeable.
- Compliance claims (ISO 27001, SOC 2, ISO 30107-3 liveness) only when the vendor states them.

## What gets rejected

- Affiliate links. Vendor homepage only.
- Duplicate entries. Update the existing row.
- Legal assertions about what a given jurisdiction requires. Link the regulator, do not paraphrase the law into advice.

## Setup

```bash
pip install pyyaml
python render_table.py          # preview
python render_table.py --write  # write into README.md
```
