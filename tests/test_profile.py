
import os
import pytest

from pkgstack.profile import Profile

TESTS_PATH = os.path.realpath(os.path.dirname(__file__))


def test_profile_create():

    config = Profile(os.path.join(TESTS_PATH, 'resources/sample.yml')).config
    assert config == [
        {'install': 'pytest', 'stage': 'test'},
        {'name': 'Install pytest-cov', 'install': 'pytest-cov', 'stage': 'test'},
        {'name': 'Install codecov', 'install': 'codecov', 'alternatives': ['test1', 'test2'], 'stage': 'test'},
        {'name': 'Install dtguess', 'install': 'dtguess==0.1.3'},
        {'install': 'dtguess==0.1.3',
            'alternatives': ['https://github.com/ownport/dtguess/releases/download/v0.1.3/dtguess-0.1.3.tar.gz'],
        }
    ]


def test_process():

    assert Profile(os.path.join(TESTS_PATH, 'resources/sample.yml')).process() == {
        'packages.successed': 1,
        'packages.failed': 1,
        'packages.total': 5
    }


def test_profile_process_via_stage():

    assert Profile(os.path.join(TESTS_PATH, 'resources/sample.yml'), stages=['test',]).process() == {
        'packages.successed': 5,
        'packages.failed': 0,
        'packages.total': 5
    }


def test_profile_incorrect_stage_type():

    with pytest.raises(RuntimeError):
        p = Profile(os.path.join(TESTS_PATH, 'resources/sample.yml'), stages='test')


def test_profile_no_deps():

    config = Profile(os.path.join(TESTS_PATH, 'resources/sample-no-deps.yml')).config
    assert config == [
        {'install': 'requests', 'name': 'install requests package w/o deps', 'no-deps': True}
    ]


def test_process_profile_no_deps():

    assert Profile(os.path.join(TESTS_PATH, 'resources/sample-no-deps.yml')).process() == {
        'packages.successed': 1,
        'packages.failed': 0,
        'packages.total': 1
    }
