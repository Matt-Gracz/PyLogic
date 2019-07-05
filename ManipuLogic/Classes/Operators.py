#!/usr/bin/python
from Propositions import ComplexProp, SimpleProp, PropTypes
from BaseClasses import Operator

#< ----------- Functions to represent operations/operators over the domain of propositions,
#              e.g., negation or material IMPL ----------- >

class BinaryOperators():
    DISJUNCT = " OR "
    CONJUCT = " AND "
    IMPL = " => "
    XOR = " (+) "
    opList = [DISJUNCT, CONJUCT, IMPL, XOR]

class PropositionalOperator(Operator):
    """ Encodes all operator in propositional logic, e.g., negation, CONJUCT, etc... """
    
    def negate(self, proposition):
        """ Applies the unary operation of negation to an arbitrary instance of any subclass
            of Proposition.
        """
        from Laws import DemorgansLaw
        if(proposition.getPropType() == PropTypes.SIMPLE):
            newProp = SimpleProp()
            newProp.rawData = "~"+proposition.rawData
        elif(proposition.getPropType() == PropTypes.COMPLEX):
            newProp = ComplexProp(proposition.rawData, proposition.operator, proposition.secondProp)
            #newProp.rawData = "~" + "(" + proposition.rawData
            #newProp.operator = proposition.operator
            #newProp.secondProp = proposition.secondProp + ")"
            DL = DemorgansLaw()
            newProp = DL.applyDemorgansLaw(newProp)
        else:
            raise NotImplementedError()
        return newProp

    def createBinaryOperator(self, antecdent, operator, consequent):
        """ Creates a generic ComplexProp of the form (antecdent, operator, consequent)
        """
        cp = ComplexProp(~antecdent, operator, ~consequent)
        return cp

    def disjoin(self, antecedent, consequent):
        """ Creates a ComplexProp of the form (antecdent, OR, consequent)
        """
        cp = self.createBinaryOperator(antecedent, BinaryOperators.DISJUNCT, consequent)
        return cp

    def conjoin(self, antecedent, consequent):
        """ Creates a ComplexProp of the form (antecdent, AND, consequent)
        """
        cp = self.createBinaryOperator(antecedent, BinaryOperators.CONJUCT, consequent)
        return cp

    def imply(self, antecedent, consequent):
        """ Creates a ComplexProp of the form (antecdent, =>, consequent)
        """
        cp = self.createBinaryOperator(antecedent, BinaryOperators.IMPL, consequent)
        return cp

    def xor(self, antecdent, consequent):
        """ Creates a ComplexProp of the form (antecdent (+) conseqent)
        """
        cp = self.createBinaryOperator(antecdent, BinaryOperators.XOR, consequent)
        return cp


