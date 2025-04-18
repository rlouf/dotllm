import logging

from dotcfg import (
    Vocabulary,
    Guide,
    PartialLark,
    CFGVocabularyIndex,
    PartialParser,
)

logger = logging.getLogger("dotllm.processors.dotgrammar")


def compile_grammar(model_name: str, grammar: str):
    logger.info("Compiling grammar index...")
    lp = PartialLark(
        grammar,
        parser="lalr",
        deterministic=True,
        start="value",
        lexer="basic",
        lazy_build_scanner_fsm=False,
    )
    parser = PartialParser.from_lark(lp)
    vocabulary = Vocabulary.from_pretrained(model_name)
    index = CFGVocabularyIndex.build(parser, vocabulary)
    guide = Guide(index)
    logger.info("Grammar index compilation complete")
    return guide
