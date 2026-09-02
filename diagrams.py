# -*- coding: utf-8 -*-
"""Bespoke per-lesson diagrams (batches A-F). render(topic_id) -> html or ''."""
from diagrams_partA import DIAGRAMS as _A
from diagrams_partB import DIAGRAMS as _B
from diagrams_partC import DIAGRAMS as _C
from diagrams_partD import DIAGRAMS as _D
from diagrams_partE import DIAGRAMS as _E
from diagrams_partF import DIAGRAMS as _F

DIAGRAMS = {}
for _d in (_A, _B, _C, _D, _E, _F):
    DIAGRAMS.update(_d)


def render(topic_id):
    fn = DIAGRAMS.get(topic_id)
    return fn() if fn else ""
