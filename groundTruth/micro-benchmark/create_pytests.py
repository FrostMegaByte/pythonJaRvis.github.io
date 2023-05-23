#!/usr/bin/env python3

import os

FILE_DIR = os.path.dirname(os.path.relpath(__file__))
SNIPPETS_DIR = os.path.join(FILE_DIR, "snippets")

base_template = """\
from base import TestBase


class {cls}Test(TestBase):
    snippet_dir = "{dir}"
"""

test_template = """
    def test_{name}(self):
        self.validate_snippet(self.get_snippet_path("{name}"))
"""


def create_test_case(name):
    test_name = name + "_test.py"
    capitalized = "".join([x.title() for x in name.split("_")])
    template = base_template.format(cls=capitalized, dir=name)

    for directory in os.listdir(os.path.join(SNIPPETS_DIR, name)):
        if directory == "." or directory == "..":
            continue
        template += test_template.format(name=directory)

    with open(os.path.join(FILE_DIR, test_name), "w+") as f:
        f.write(template)


def create_new_test_case(name):
    test_name = f"new_{name}_test.py"
    capitalized = "".join([x.title() for x in name.split("_")])
    template = base_template.format(cls=f"New{capitalized}", dir=f"newCase/{name}")

    for directory in os.listdir(os.path.join(SNIPPETS_DIR, "newCase", name)):
        if directory == "." or directory == "..":
            continue
        template += test_template.format(name=directory)

    with open(os.path.join(FILE_DIR, test_name), "w+") as f:
        f.write(template)


def main():
    for name in os.listdir(SNIPPETS_DIR):
        if (
            not os.path.isdir(os.path.join(SNIPPETS_DIR, name))
            or name == "."
            or name == ".."
        ):
            continue

        if name == "newCase":
            for new_name in os.listdir(os.path.join(SNIPPETS_DIR, "newCase")):
                create_new_test_case(new_name)
        else:
            create_test_case(name)


if __name__ == "__main__":
    main()
