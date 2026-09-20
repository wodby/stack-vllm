"""Check the composition contract without importing or deploying a stack."""
from pathlib import Path
import unittest
import yaml


class ContractTest(unittest.TestCase):
    def test_private_single_runtime(self):
        root = Path(__file__).parents[1]
        stack = yaml.safe_load((root / "stack.yml").read_text())
        self.assertEqual(stack["access"], {"required": True, "mode": "private_network", "scope": "entire_app"})
        self.assertEqual(stack["services"], [{"name": "vllm", "title": "vLLM", "service": "vllm", "required": True, "main": True, "replicas": 1}])
        readme = (root / "README.md").read_text()
        self.assertEqual(readme.count("<!-- wodby:generated:start -->"), 1)
        self.assertEqual(readme.count("<!-- wodby:generated:end -->"), 1)


if __name__ == "__main__":
    unittest.main()
