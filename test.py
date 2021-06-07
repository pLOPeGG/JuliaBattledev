import subprocess
import time

from contextlib import contextmanager
from dataclasses import dataclass
from glob import glob
from pathlib import Path

import pytest

ext_to_interpreter = {
    ".jl": "julia",
    ".py": "python",
}


@dataclass
class Job:
    interpreter: str
    source_code: Path
    input_test: Path
    output_test: Path

    def run(self):
        args = [self.interpreter, str(self.source_code)]
        with self.input_test.open("r", encoding="utf8") as fp_input:
            res_run = subprocess.run(args, capture_output=True, stdin=fp_input, timeout=2.0)
        res_out = res_run.stdout.decode()
        # log stderr

        with self.output_test.open("r", encoding="utf8") as fp_output:
            expected_out = "\n".join(fp_output.readlines())

        return res_out.strip(), expected_out.strip()

@contextmanager
def timeit(job: Job):
    beg = time.time()
    yield
    assert time.time() - beg < 1.0, ("timeout", job.input_test.name, job.input_test.open("r").readlines())

def fetch_job(solution: Path, test_case: str) -> Job:
    solution = solution
    return Job(
        ext_to_interpreter[solution.suffix],
        solution,
        solution.parent / f"{solution.name.split('.')[0]}_files" / f"input{test_case}.txt",
        solution.parent / f"{solution.name.split('.')[0]}_files" / f"output{test_case}.txt",
        )

def fetch_all_jobs(solution: Path, test_case: str) -> list[Job]:
    if test_case == "*":
        suffixes = [
            file.name[5:-4]
            for file in (solution.parent / f"{solution.name.split('.')[0]}_files").glob("input*.txt")
        ]
        return [fetch_job(solution, test_case_i) for test_case_i in suffixes]
    else:
        return [fetch_job(solution, test_case)]


def test_solutions(solution: Path, test_case: str):
    for job in fetch_all_jobs(solution, test_case):
        with timeit(job):
            res, exp = job.run()
        assert res == exp, ("wrong answer", job.input_test.name, job.input_test.open("r").readlines())