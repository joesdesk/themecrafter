import pytest

import xml.etree.ElementTree as ET
from themecrafter.nlp import NLTKPlain, StanfordPlain

docs = BGSurveyDataSet().X


def test_NLTKPlain():
    
    processor = NLTKPlain()
    elem = processor.parse_corpus(docs)
    assert type(elem) is ET.Element


def test_StanfordPlain():
    
    processor = NLTKPlain()
    elem processor.parse_corpus(docs)
    assert type(elem) is ET.Element
    
    