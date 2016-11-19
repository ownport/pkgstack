
import os
import sys
import pytest

from pkgstack.profile import Profile

TESTS_PATH=os.path.realpath(os.path.dirname(__file__))

def test_profile_create(tmpdir):

    assert Profile(os.path.join(TESTS_PATH, 'resources/sample.yml')).config == [
        {'install': 'pytest',},
        {'name': 'Install pytest-cov', 'install': 'pytest-cov'},
        {'name': 'Install codecov', 'install': 'codecov', 'alternatives': ['test1', 'test2']},
        {'name': 'Install dtguess', 'install': 'dtguess==0.1.3',},
        {'install': 'dtguess==0.1.3',
            'alternatives': ['https://github.com/ownport/dtguess/releases/download/v0.1.3/dtguess-0.1.3.tar.gz'],
        }
    ]


def test_process():

    assert Profile(os.path.join(TESTS_PATH, 'resources/sample.yml')).process() == {
        'packages.successed': 4,
        'packages.failed': 1,
        'packages.total': 5
    }
