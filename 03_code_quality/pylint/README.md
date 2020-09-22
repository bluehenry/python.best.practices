#[Pylint](https://www.pylint.org/)
[Pylint](https://www.pylint.org/) is used as a static analysis tool for Python code. Pylint checks coding standard(PEP 8 -- Style Guide for Python Code), detect errors and provide refactoring help.

The Pylint message type can be:
* [R]efactor for a “good practice” metric violation
* [C]onvention for coding standard violation
* [W]arning for stylistic problems, or minor programming issues
* [E]rror for important programming issues (i.e. most probably bug)
* [F]atal for errors which prevented further processing

## Best Practice
### [W1203 with F-strings](https://github.com/PyCQA/pylint/issues/2354)
No need to correct f-string, because f-strings have many other advantages over % formatting from a readability and/or flexibility perspective.

## Disable some style checking
Add the following in .py file
```
pylint: disable=C0301
```

