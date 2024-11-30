import pytest
from pascal import Namespace


@pytest.fixture
def namespaces(scope="function") -> tuple[Namespace, Namespace]:
    parent = Namespace()
    c1 = Namespace(parent=parent)
    c2 = Namespace(parent=parent)
    parent.add_inner(c1)
    parent.add_inner(c2)

    parent.variables = {'a': 1}
    c1.variables = {'b': 1, 'c': 2}
    c2.variables = {'b': 3, 'c': 4}

    return parent, c1


class TestNamespace:

    def test_json(self, namespaces):
        parent, child = namespaces

        assert parent.to_json() == {
            'vars': {'a': 1},
            'inners': [
                {'vars': {'b': 1, 'c': 2}},
                {'vars': {'b': 3, 'c': 4}}
            ]
        }

        assert child.get('d') is None
