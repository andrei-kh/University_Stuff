#!/usr/bin/env python3

import simple_match

import unittest

import re

MATCH = 'match'
SEARCH = 'search'
FINDALL = 'findall'
SUB = 'sub'


def regexp_test(module):
    def decorator(clazz):
        def gen_test(regexp, method, matches, not_matches=None):
            def test(self):
                _regexp = re.compile(getattr(module, regexp))
                if method == SUB:
                    _repl = getattr(module, regexp + '_REPL')
                if method == MATCH:
                    for t in matches:
                        self.assertTrue(not not _regexp.match(t))
                    for t in not_matches:
                        self.assertFalse(not not _regexp.match(t))
                elif method == SEARCH:
                    for (k, v) in matches.items():
                        self.assertEqual(v, _regexp.search(k).group())
                elif method == FINDALL:
                    for (k, v) in matches.items():
                        self.assertEqual(v, _regexp.findall(k))
                elif method == SUB:
                    for (k, v) in matches.items():
                        self.assertEqual(v, _regexp.sub(_repl, k))
                else:
                    raise Exception("Unknown re method")
            return test

        for (k, v) in clazz.TEST_DATA.items():
            setattr(clazz, 'test_' + k, gen_test(k, *v))

        return clazz
    return decorator


@regexp_test(simple_match)
class SimpleMatchTest(unittest.TestCase):
    TEST_DATA = {
        'REGEXP_1': (    # название тестируемого регулярного выражения
            MATCH,       # тип тестируемого метода — MATCH для этого файла
            ['a', 'ab'],  # список строк, соответствующих шаблону
            ['b', 'ba']  # список строк, не соответствующих шаблону
        ),
        'REGEXP_2': (
            MATCH,
            ['aab', 'abb', 'acb'],
            ['ab', 'aabc']
        ),
        'REGEXP_3': (
            MATCH,
            ['sofia.mp3', 'sofia.mp4'],
            ['sofia.mp7', 'sofia.mp34']
        ),
        'REGEXP_4': (
            MATCH,
            ['taverna', 'versus', 'vera', 'zveri'],
            ['zver']
        ),
        'REGEXP_5': (
            MATCH,
            ['aaa', 'bbb'],
            ['a', 'aa', 'aaaa', 'b', 'bb', 'bbbb']
        ),
        'REGEXP_6': (
            MATCH,
            ['OkOkOk', 'ababab'],
            ['Ok', 'OkOk', 'OkOkOkOk', 'ab', 'abab', 'abababab']
        ),
        'REGEXP_7': (
            MATCH,
            ['aaa Aaa aaa', 'aaa aaa Aaa', 'Aaa aaa aaa'],
            ['aaa', 'aaa aaa', 'A', 'aaa A aaa']
        ),
        'REGEXP_8': (
            MATCH,
            ['abc', 'abc03', 'a-b-c-3', 'a.b.c.0'],
            ['Aabc', 'abc1', '#abc']
        )
    }


if __name__ == '__main__':
    unittest.main()
