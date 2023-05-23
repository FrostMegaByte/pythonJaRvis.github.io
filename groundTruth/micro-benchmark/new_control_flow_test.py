from base import TestBase


class NewControlFlowTest(TestBase):
    snippet_dir = "newCase/control_flow"

    def test_elseif(self):
        self.validate_snippet(self.get_snippet_path("elseif"))

    def test_if(self):
        self.validate_snippet(self.get_snippet_path("if"))

    def test_ifMain(self):
        self.validate_snippet(self.get_snippet_path("ifMain"))

    def test_while(self):
        self.validate_snippet(self.get_snippet_path("while"))

    def test_with(self):
        self.validate_snippet(self.get_snippet_path("with"))
