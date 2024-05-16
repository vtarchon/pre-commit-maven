import argparse
import os.path
from pre_commit_maven.utils import maven


def execute(goals: list, cwd: str, maven_helper=maven):
    execution_result = maven_helper.execute(goals, cwd)
    if execution_result.return_code != 0:
        maven_helper.print_error(execution_result)
    else: 
        for line in execution_result.stdout.splitlines():
            print_fn(f"{line}")
    return execution_result.return_code
