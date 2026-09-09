# 01 – Random Number

Ask the user for a number between 1 and 10, validate it, generate some random
numbers in the same range, and report whether any of them match.

## Files

- `random_num_check.py` – generates 5 random numbers and checks them against the guess
- `main.py` – earlier variant that generates a single random number

## Run

```bash
python random_num_check.py
```

## Known issues / TODO

- `main.py`: `import boolean` is an unused third-party import; the plain
  `match = False` already does the job, so the import can be removed.
- `main.py`: the loop iterates `range(1, generated_nums + 1)` (the *value* of the
  random number) instead of a list of generated numbers, so the match logic and
  the repeated "thanks for playing" print are both off.
- `random_num_check.py`: `for i in range(random_num)` fails because `random_num`
  is a list — it should be `for i in random_num`. `import array` is unused.
