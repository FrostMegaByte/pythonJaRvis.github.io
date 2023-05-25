import os
import sys
import importlib
import json
import sys
from unittest import TestCase, main
from dotenv import load_dotenv

sys.path.insert(1, "../../Jarvis")
import Jarvis.utils as utils
from Jarvis.pythoncg import CallGraphGenerator

load_dotenv()


class TestBase(TestCase):
    snippet_dir = ""

    def get_snippet_path(self, name):
        return os.path.join(os.environ.get("SNIPPETS_PATH"), self.snippet_dir, name)

    def validate_snippet(self, snippet_path):
        output = self.get_snippet_output_cg(snippet_path)
        expected = self.get_snippet_expected_cg(snippet_path)
        self.assertEqual(output, expected)

    def get_snippet_output_cg(self, snippet_path):
        main_path = os.path.join(snippet_path, "main.py")
        try:
            cg = CallGraphGenerator(
                entry_points=[main_path],
                package=snippet_path,
                max_iter=-1,
                operation=utils.constants.CALL_GRAPH_OP,
            )
            cg.analyze()
            output = cg.output()
            output_cg = {}
            for node in output:
                output_cg[node] = list(output[node])
            with open(os.path.join(snippet_path, "pythonCG.json"), "w") as f:
                json.dump(output_cg, f)
            return output
        except Exception as e:
            raise e

    def get_snippet_output_cg_from_file(self, snippet_path):
        cg_path = os.path.join(snippet_path, "pythonCG.json")
        with open(cg_path, "r") as f:
            return json.loads(f.read())

    def get_snippet_expected_cg(self, snippet_path):
        cg_path = os.path.join(snippet_path, "callgraph.json")
        with open(cg_path, "r") as f:
            return json.loads(f.read())

    def assertEqual(self, actual, expected):
        def do_sorted(d):
            s = {}
            for n in d:
                if not d[n]:
                    continue
                s[n] = sorted(d[n])
            return s

        super().assertEqual(do_sorted(actual), do_sorted(expected))


if __name__ == "__main__":
    main()
