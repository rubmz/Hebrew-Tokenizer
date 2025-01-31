#!/usr/bin/env python
# encoding: utf-8
import sys
import os
print(os.path.abspath(os.getcwd()))
sys.path.append(os.path.abspath(os.getcwd()))
from hebrew_tokenizer.tokenizer import tokenizer


def tokenize(text, with_whitespaces=False):
    tokenizer.with_whitespaces = with_whitespaces
    return tokenizer.tokenize(text)


if __name__ == '__main__':
    sent = 'מָתֵמָטִיקָה זה קשה'
    sent_tokens = tokenize(sent)
    for st in sent_tokens:
        print(st)

