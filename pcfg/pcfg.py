from typing import Iterator, List, Tuple, Union
import random
import nltk  # type: ignore
from nltk.grammar import ProbabilisticProduction  # type: ignore
from nltk.grammar import Nonterminal  # type: ignore
import sys

Symbol = Union[str, Nonterminal]

class PCFG(nltk.grammar.PCFG):
    def generate(self, start=None, depth=None, n=None):
        """
            Generates an iterator of all sentences from a CFG.

            :param grammar: The Grammar used to generate sentences.
            :param start: The Nonterminal from which to start generate sentences.
            :param depth: The maximal depth of the generated tree.
            :param n: The maximum number of sentences to return.
            :return: An iterator of lists of terminal tokens.
        """
        if not start:
            start = self.start()
        if depth is None:
            depth = sys.maxsize

        # Added: since now it's one-branch exploration, iterate it for N sentences
        if n == None: n = 1
        for i in range(n):
            for s in self._generate_all([start], depth): yield s

    def _generate_all(self, items, depth):
        """
            Recursive generation for a sequence of RHS symbols
        """
        if items:
            try:
                for frag1 in self._generate_one(items[0], depth):
                    for frag2 in self._generate_all(items[1:], depth):
                        yield frag1 + frag2
            except RecursionError as error:
                raise RuntimeError(
                    "The grammar has rule(s) that yield infinite recursion!"
                ) from error
        else:
            yield []


    def _generate_one(self, item, depth):
        """
            Symbol resolution with branching factor: 1
        """
        if depth > 0:
            if isinstance(item, Nonterminal):
                productions = self.productions(lhs=item)
                # Added: instead of iterating productions equally, randomly sample
                prod = random.choices(productions, weights=[p.prob() for p in productions])[0]
                yield from self._generate_all(prod.rhs(), depth - 1)
            else:
                yield [item]
