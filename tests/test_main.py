
import os
import sys

from pkgstack.main import process
from pkgstack.main import read_config

TESTS_PATH=os.path.realpath(os.path.dirname(__file__))


def test_read_config():

    assert read_config(os.path.join(TESTS_PATH, 'resources/sample.yml')) == [
        {'install': 'pytest',},
        {'name': 'Install pytest-cov', 'install': 'pytest-cov'},
        {'name': 'Install codecov', 'install': 'codecov', 'alternatives': ['test1', 'test2']},
        {'name': 'Install dtguess', 'install': 'dtguess==0.1.3',},
        {'install': 'dtguess==0.1.3',
            'alternatives': ['https://github.com/ownport/dtguess/releases/download/v0.1.3/dtguess-0.1.3.tar.gz'],
        }
    ]


def test_process():

    configfile_path = os.path.join(TESTS_PATH, 'resources/sample.yml')
    assert process(read_config(configfile_path)) == {
        'packages.successed': 4,
        'packages.failed': 1,
        'packages.total': 5
    }
