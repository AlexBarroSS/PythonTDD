
import re
from re import findall, match
from typing import Pattern


def formated_print(name, params, return_):
    print(
        f"function: {name}() \n params ->  {params} \n return -> ({return_})")


def raws():
    # classes de caracteres - rodar no compilador python 3.9.5
    name = "Alex Barros Silva"

    findall('[aeiou]', name)
    findall('[^aeiou]', name)

    findall('[a-f]', name)
    findall('[a-fA-Z]', name)
    findall('[a-zA-Z]', name)

    # equal
    findall('[a-zA-Z0-9_]', name)
    findall('[\w]', name)
    findall('\w', name)

    # raw string

    raws = '\section\n'

    print(match(r'\\section', raws))
    print(match('a|e', name))

    first_html = '<input type="text" id="id_cpf" name="cpf">'
    second_html = '<input id="id_cpf" name="cpf" type="text" >'

    pattern = r'<(?P<tag>.+?) (?:(?:type="(?P<type>.+?)"|id="(?P<id>.+?)"|name="(?P<name>.+?)") ?)*'

    mat = match(pattern, second_html)

    mat.groups()
    mat.groupdict()

    formated_print('groups', '', mat.groups())
    formated_print('groupdict', '', mat.groupdict())


def run_formated_print():
    formated_print('match', ('.', '\n'), re.match('.', '\n'))

    formated_print('match', ('^.$', 'A'), re.match('^.$', 'A'))

    formated_print('findall', ('^.', 'abc\ndese\nfsd'),
                   re.findall('^.', 'abc\ndese\nfsd'))

    formated_print('findall', ('.$', 'abc\ndese\nfsd'),
                   re.findall('.$', 'abc\ndese\nfsd'))

    formated_print('findall', ('^$', '\n'),
                   re.findall('^$', '\n', re.MULTILINE))


if __name__ == '__main__':
    raws()
