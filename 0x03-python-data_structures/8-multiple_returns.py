#!/usr/bin/python3
def multiple_returns(sentence):
    ln = len(sentence)
    if ln == 0:
        ret = (ln, None)
        return (ret)
    ret = (ln, sentence[0])
    return ret
