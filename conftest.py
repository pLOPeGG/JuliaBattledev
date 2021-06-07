from pathlib import Path

from pytest import fixture


def pytest_addoption(parser):
    parser.addoption(
        "--solution",
        action="store"
    )
    parser.addoption(
        "--test_case",
        action="store",
        default="*"
    )


@fixture()
def solution(request):
    return Path(request.config.getoption("--solution"))


@fixture()
def test_case(request):
    return request.config.getoption("--test_case")
