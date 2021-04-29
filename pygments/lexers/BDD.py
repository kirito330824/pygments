from pygments.lexer import RegexLexer
from pygments.token import *

class BDDLexer(RegexLexer):
    name = 'BDD'
    aliases = ['bdd']
    filenames = ['*.feature']

    tokens = {
        'root': [
            (r' .*\n', Text),
            (r'\+.*\n', Generic.Inserted),
            (r'-.*\n', Generic.Deleted),
            (r'@.*\n', Generic.Subheading),
            (r'Index.*\n', Generic.Heading),
            (r'=.*\n', Generic.Heading),
            (r'.*\n', Text),
        ]
        'keywords': [
            (words((
                'When', 'And', 'Then', 'Given', 'Scenario', 'Background', 'Feature',
              ), perfix=r'\b'),
             Keyword),
            (words(('True', 'False', 'None'), suffix=r'\b'), Keyword.Constant),
        ],
    }