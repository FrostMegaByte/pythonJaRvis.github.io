from base import TestBase


class NewImportTest(TestBase):
    snippet_dir = "newCase/import"

    def test_chain_import(self):
        self.validate_snippet(self.get_snippet_path("chain_import"))

    def test_import_all(self):
        self.validate_snippet(self.get_snippet_path("import_all"))

    def test_import_as(self):
        self.validate_snippet(self.get_snippet_path("import_as"))

    def test_import_same(self):
        self.validate_snippet(self.get_snippet_path("import_same"))

    def test_init_import(self):
        self.validate_snippet(self.get_snippet_path("init_import"))
