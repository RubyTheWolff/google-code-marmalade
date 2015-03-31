'''Handle input'''

import inspect
from itertools import islice
import os

_JAM_DIRECTORY = os.path.dirname(os.path.realpath(__file__)) 
_INPUT_FILE = _JAM_DIRECTORY + "/input.txt"
_OUTPUT_FILE = _JAM_DIRECTORY + "/output.txt"

def read_test_case(f, main_fn, test_length_fn):
    test_length, lines_read = test_length_fn(f, main_fn)
    test_arguments = lines_read + list(islice(f, int(test_length)))
    rstripped = (x.rstrip('\n') for x in test_arguments)
    return tuple(rstripped)

def write_result(i, result):
    output_line = "Case #%d: %s\n" % (i, str(result))
    with open(_OUTPUT_FILE, 'a') as out_f:
        out_f.write(output_line)

def default_test_length(f, main_fn):
    fn_spec = inspect.getargspec(main_fn) 
    fn_arity = len(fn_spec[0])
    return fn_arity, []

def first_line_test_length(f, main_fn):
    first_line = f.readline()
    return first_line, [first_line]

def output(main_fn, test_length_fn = default_test_length):
    try:
        os.remove(_OUTPUT_FILE)
    except FileNotFoundError:
        pass

    with open(_INPUT_FILE) as f:
        num_test_cases = int(f.readline())
        for i in range(1, num_test_cases + 1):
            case = read_test_case(f, main_fn, test_length_fn)
            result = main_fn(*case)
            write_result(i, result)
            print("Test case %d done" % i)
    print("Done!")
