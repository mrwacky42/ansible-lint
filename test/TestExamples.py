"""Assure samples produced desire outcomes."""
import pytest

from ansiblelint.runner import Runner


def test_example(default_rules_collection):
    """example.yml is expected to have 15 match errors inside."""
    result = Runner(
        'examples/playbooks/example.yml', rules=default_rules_collection
    ).run()
    assert len(result) == 15


@pytest.mark.parametrize(
    "filename",
    (
        pytest.param(
            'examples/playbooks/syntax-error-string.yml', id='syntax-error-string'
        ),
        pytest.param('examples/playbooks/syntax-error.yml', id='syntax-error'),
    ),
)
def test_example_syntax_error(default_rules_collection, filename):
    """Validates that loading valid YAML string produce error."""
    result = Runner(filename, rules=default_rules_collection).run()
    assert len(result) >= 1
    passed = False
    for match in result:
        if match.rule.id == "syntax-check":
            passed = True
    assert passed, result


def test_example_custom_module(default_rules_collection):
    """custom_module.yml is expected to pass."""
    result = Runner(
        'examples/playbooks/custom_module.yml', rules=default_rules_collection
    ).run()
    assert len(result) == 0
