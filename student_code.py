import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        print("Asserting {!r}".format(fact))
        # first, check if already in list; main.py setup already checks if it is a fact
        if fact not in self.facts:
            self.facts.append(fact)
        else:
            print("fact already asserted, you fool!")
        
    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        print("Asking {!r}".format(fact))
        answers_list = ListOfBindings()
        query_statement = fact.statement
        """# see if just asking for an exact fact
        if (not is_var(fact.statement.terms[0])) and (not is_var(fact.statement.terms[1])):
            if fact in self.facts:
                return answers_list
            else:
                return False"""
        # iterate through kb list of facts to find a match to all variables
        for assertion in self.facts:
            asserted_statement = assertion.statement
            answer = match(query_statement, asserted_statement)     # match returns bindings or false
            if answer:
                answers_list.add_bindings(answer)
        if answers_list:
            return answers_list
        else:
            return False
