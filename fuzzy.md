# Fuzzy Finding

- Technique that helps finding matching results of imperfect
search terms

# Primitive operations

- How close a given input is from a result is determined by the amount of primitive operations necessary to convert the input string into an exact match. This is called 'Edit distance'

- Insertion:
> cot -> coat
> co\*t -> coat

- Deletion:
> coat -> cot
> coat -> co\*t

- Substitution:
> coat -> cost

> All methods can be expressed as substitutions if a \* is used to
represent a NULL character

# Levenshtein Distance

Levenshtein distance a metric for mesuring the minimum number of single-character (primitives) edits needed to transform an input text into a given answer



