'''Handle input'''

import inspect
from itertools import islice
import os

_INPUT_FILE = os.path.dirname(os.path.realpath(__file__)) + "/input.txt"
_OUTPUT_FILE = os.path.dirname(os.path.realpath(__file__)) + "/output.txt"

def read_test_case(f, main_fn, test_length_fn):
    test_length, lines_read = test_length_fn(f, main_fn)
    return tuple(lines_read + list(islice(f, fn_arity)))

def write_result(i, result):
    output_line = "Case #%d: %s" % (i, str(result))
    with open(_OUTPUT_FILE, 'a') as out_f:
        out_f.write(output_line)

def default_test_length(f, main_fn):
    fn_spec = inspect.getargspec(main_fn) 
    fn_arity = len(fn_spec[0])
    return fn_arity, []

def first_line_test_length(f, main_fn):
    first_line = int(f.readline())
    return first_line, [first_line]

def output(main_fn, test_length_fn = default_test_length):
    with open(_INPUT_FILE) as f:
        num_test_cases = int(f.readline())
        for i in range(num_test_cases):
            case = read_test_case(f, main_fn, test_length_fn)
            result = main_fn(*case)
            write_result(result)
