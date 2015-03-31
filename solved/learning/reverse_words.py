#!/usr/bin/env python3

import marmalade

def set_arg_types(words):
    '''All arguments from the input file are by default passed as strings.
    Remember to cast the arguments to the correct types.'''
    return str(words)

def reverse_words(words):
    words = set_arg_types(words)

    word_list = words.split(' ')
    return ' '.join(reversed(word_list))

def main():
    marmalade.output(reverse_words)

if __name__ == '__main__':
    main()
