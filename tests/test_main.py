
import os
import sys
import pytest
import argparse

from pkgstack.main import process

TESTS_PATH=os.path.realpath(os.path.dirname(__file__))

class MockedArgParser(object):

    def print_help(self):
        sys.exit(1)


class MockedParserArgs(object):

    def __init__(self, profile=None, stage=None, logging=None):
        self._profile = profile
        self._stage = stage
        self._logging = logging

    @property
    def profile(self):
        return self._profile

    @property
    def stage(self):
        return self._stage

    @property
    def logging(self):
        return self._logging



def test_main_process_no_args(monkeypatch):

    monkeypatch.setattr(argparse, 'ArgumentParser', MockedArgParser)
    parser = argparse.ArgumentParser()
    with pytest.raises(SystemExit):
        process(parser, MockedParserArgs())


def test_main_process_only_logging(monkeypatch):

    monkeypatch.setattr(argparse, 'ArgumentParser', MockedArgParser)
    parser = argparse.ArgumentParser()
    with pytest.raises(SystemExit):
        process(parser, MockedParserArgs(logging='DEBUG'))


def test_main_process_incorrect_logging(monkeypatch):

    monkeypatch.setattr(argparse, 'ArgumentParser', MockedArgParser)
    parser = argparse.ArgumentParser()
    with pytest.raises(SystemExit):
        process(parser, MockedParserArgs(logging='TEST'))


def test_main_process_profile(monkeypatch):

    monkeypatch.setattr(argparse, 'ArgumentParser', MockedArgParser)
    parser = argparse.ArgumentParser()
    assert process(parser, MockedParserArgs(logging='DEBUG',
        profile=[os.path.join(TESTS_PATH, 'resources/sample-cmd.yml'),])) == [{'packages.failed': 0, 'packages.successed': 1, 'packages.total': 2}]


def test_main_process_profile_with_stages(monkeypatch):

    monkeypatch.setattr(argparse, 'ArgumentParser', MockedArgParser)
    parser = argparse.ArgumentParser()
    assert process(parser, MockedParserArgs(logging='DEBUG', stage=['test',],
        profile=[os.path.join(TESTS_PATH, 'resources/sample-cmd.yml'),])) == [{'packages.failed': 0, 'packages.successed': 2, 'packages.total': 2}]


def test_main_process_profile_does_not_exist(monkeypatch):

    monkeypatch.setattr(argparse, 'ArgumentParser', MockedArgParser)
    parser = argparse.ArgumentParser()
    assert process(parser, MockedParserArgs(logging='DEBUG',
        profile=[os.path.join(TESTS_PATH, 'resources/none.yml'),])) == []
