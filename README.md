# DPLL SAT Solver

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple [SAT](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem) Solver implemented with [DPLL Algorithm](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem#Algorithms_for_solving_SAT), developed as a project to [**IF673 - Logic Applied to Computer Science**](https://www.cin.ufpe.br/~if673/) at CIn/UFPE.

## Restrictions

Since this is just a introductory project into the vast SAT solvers field, this program has some restrictions on its input. In order to be able to return you an answer, your input must:

- Have a line informing the number of formulas to be analyzed;
- Each line must have only one formula;
- Be formatted in [**Conjunctive normal form (CNF)**](https://en.wikipedia.org/wiki/Conjunctive_normal_form);
- All clauses must be [**Horn Clauses**](https://en.wikipedia.org/wiki/Horn_clause);
- All clauses, even unitary ones, must be enclosed into brackets.
- Each binary operator ( _v_ for disjunction and _&_ for conjunction) must be separated from he literals and clauses by an empty space.
- The unary negation operator _~_ must not be separated from the literal.

## Software prerequisites

In order to run this you will need:

- Python 3

## Results

The results will be placed after the _saida.out_ file, which follows the structure:

```
Problema #X
Message
```

The _X_ stands for the problem that has been solved, starting at 1. The Message might be each one of the following:

- **Não está na FNC.** - if given formula does not follow CNF;
- **Nem todas as cláusulas são de Horn.** - if not all clauses are Horn clauses;
- **Sim, é satisfatível.** - if given formula is satisfiable
- **Não, não é satisfatível.** - if given formula is not satisfiable

## License

This project is [MIT Licensed](LICENSE)
