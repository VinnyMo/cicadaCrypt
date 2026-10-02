# cicadaCrypt

A small Python experiment for exploring the rune alphabet used in Cicada 3301's *Liber Primus*. It prints a direct rune-to-Latin transliteration, an Atbash mapping, and an experimental shifted result.

This is a puzzle-study project. It does not provide secure encryption or claim to solve *Liber Primus*.

## What's here

- [`decrypt.py`](decrypt.py): an interactive script with a 29-rune alphabet and corresponding Latin letter groups
- [`key.txt`](key.txt): the repository's reference file
- [`liber_primus_full/`](liber_primus_full/): page images and accompanying reference material

## Try the script

Use Python 3 in a terminal that supports UTF-8. There are no third-party Python imports in the script.

```bash
git clone https://github.com/VinnyMo/cicadaCrypt.git
cd cicadaCrypt
python3 decrypt.py
```

At the first prompt, enter runes from the script's `RUNES` list. At the second, enter an integer shift. For a small example, enter `ᚠ-ᚢ/ᚦ` and then `0`.

The input convention is:

| Input | Meaning |
| --- | --- |
| A supported rune | Look up its Latin letter group |
| `-` | A space within an output line |
| `/` or `.` | End the current output line |

Ordinary spaces and unsupported characters are not accepted by the rune lookup. The script prints Python lists for the direct and Atbash results.

## How the experiment works

1. **Direct transliteration:** use the rune's index to select an entry from `LETTERS`
2. **Atbash:** reverse that position in the 29-entry alphabet
3. **Shifted Atbash:** attempt a modular shift over the Atbash output

The final stage operates character by character even though some entries in `LETTERS` are multi-character groups, such as `TH` or `V(U)`. It can therefore raise `ValueError` for otherwise supported rune input. The first two stages are useful to inspect independently; the shifted stage needs further work.

## Current scope

The code is a compact, interactive experiment with hard-coded mappings. There is no command-line argument parser, input-validation layer, automated test suite, or general-purpose decryption pipeline. The page images are reference material; the script does not read them or perform OCR.

No license file is included in this repository. Check permissions before redistributing code or bundled reference material.
