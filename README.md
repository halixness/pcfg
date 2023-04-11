pcfg
====

Description
-----------

A knob-rich fork of [thomasbreydo/pcfg](github.com/thomasbreydo/pcfg). You can instantiate your own [PCFG](https://www.nltk.org/api/nltk.html#nltk.grammar.PCFG) with the added ``generate()`` method to probabilistically generate valid sentences. (NLTK stands for Natural Language Toolkit.)
The parameters thus are the same as [nltk.parse.generate](https://www.nltk.org/howto/generate.html).

Example usage
-------------

A ``PCFG`` can be initialized in the same way that an NLTK [probabilistic context-free grammar](https://www.nltk.org/api/nltk.html#nltk.grammar.PCFG) is initialized:

```python3
>>> from pcfg import PCFG
>>> grammar = PCFG.fromstring("""
S -> Subject Action [1.0]
Subject -> "a cow" [0.7] | "some guy" [0.1] | "the woman" [0.2]
Action -> "eats lunch" [0.5] | "was here" [0.5]
""")
```

To generate sentences, simply use the ``generate()`` method:

```python3
>>> for sentence in grammar.generate(n=3, depth=5, start=Nonterminal("S")):
...     print(sentence)
```

The output could be the following:

```text
the woman eats lunch
the woman was here
a cow was here
```

Of course, your output may be different because the sentences are generated probabilistically.

License
-------
[WTFPL](http://www.wtfpl.net)
