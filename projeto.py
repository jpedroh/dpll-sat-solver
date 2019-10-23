def isFNC(formula):
    formulas = formula[1:-1].split(') & (')
    for formula in formulas:
        if '&' in formula or '>' in formula or '<' in formula:
            return False
    return True

def isOnlyHorn(formula):
    formulas = formula[1:-1].split(') & (')
    for formula in formulas:
        literals = formula.split(' v ')
        totalPositiveLiterals = 0
        for literal in literals:
            if not '~' in literal:
                totalPositiveLiterals += 1
        if totalPositiveLiterals > 1:
            return False
    return True

def DPLL(formula):
    # Fazemos a propagação de cada cláusula unitária
    while hasUnitaryClause(formula):
        unitaryClause = getUnitaryClause(formula)
        formula.remove(unitaryClause)
        unitaryClause = list(unitaryClause)[0]
        deleteClausesContainingLiteral(unitaryClause, formula)
        deleteLiteralFromClauses((unitaryClause[0], not unitaryClause[1]), formula)
    # Verificamos se o conjunto de cláusulas está vzaio
    if len(formula) == 0:
        return True
    # Verificamos se o conjunto possui uma clausula vazia
    if set() in formula:
        return False
    
    newLiteral = list(formula[0])[0][0]
    newPositiveClause = set()
    newNegativeClause = set()

    newPositiveClause.add(( newLiteral, True ))
    newNegativeClause.add(( newLiteral, False ))

    newPositiveFormula = formula.copy()
    newPositiveFormula.append(newPositiveClause)

    newNegativeFormula = formula.copy()
    newNegativeFormula.append(newNegativeClause)

    return DPLL(newPositiveFormula) or DPLL(newNegativeFormula)

def hasUnitaryClause(formula):
    for clause in formula:
        if len(clause) == 1:
            return True
    return False

def getUnitaryClause(formula):
    for clause in formula:
        if len(clause) == 1:
            return clause
    return None

def deleteClausesContainingLiteral(literal, formula):
    for clause in formula:
        if literal in clause:
            formula.remove(clause)

def deleteLiteralFromClauses(literal, formula):
    for clause in formula:
        if literal in clause:
            clause.remove(literal)

def isSatisfiable(formula):
    formula = buildFormula(formula)
    return DPLL(formula)

def buildFormula(formula):
    formula = formula[1:-1].split(') & (')
    clauses = list()
    for clause in formula:
        clauses.append(buildClause(clause))
    return clauses

def buildClause(clauses):
    literals = clauses.split(' v ')
    clause = set()
    for literal in literals:
        if literal.startswith('~'):
            clause.add(( literal[1], True ))
        else:
            clause.add(( literal[0], False ))
    return clause

def getSmallestFormula(formulas):
    minSize = len(formulas[0])
    smallestFormula = formulas[0]

    for formula in formulas:
        if len(formula) <= minSize:
            minSize = len(formula)
            smallestFormula = formula
    return smallestFormula

def main():
    responses = []
    with open('Entrada2.in') as inputFile:
        numberOfFormulas = int(inputFile.readline())
        formulas = inputFile.readlines()
        i = 1

        for formula in formulas:
            responses.append("Problema #{}\n".format(i))

            if not isFNC(formula):
                responses.append("Não está na FNC.\n")
            elif not isOnlyHorn(formula):
                responses.append("Nem todas as cláusulas são de Horn.\n")
            elif isSatisfiable(formula):
                responses.append("Sim, é satisfatível.\n")
            else:
                responses.append("Não, não é satisfatível.\n")
            responses.append("\n")
            i = i + 1

    with open('saida.out', 'w') as outputFile:
        outputFile.writelines(responses)

if __name__ == "__main__":
    main()