import pytest
from notation import Notations


class TestNotations:
    @pytest.mark.parametrize(
        "s, result",
        [("+ - 13 4 55", "13 + 4 - 55"),
         ("+ 2 * 2 - 2 1", "2 + 2 * 2 - 1"),
         ("+ + 10 20 30", "10 + 20 + 30"),
         ("/ + 3 10 * + 2 3 - 3 5", "3 / 10 + 2 * 3 + 3 - 5"),
         ("1.5 - - - 1 4.5 3", "1.5 - 1 - 4.5 - 3")]
    )
    def test_result(self, s, result):
        assert Notations.to_infix_notation(s) == result

    @pytest.mark.parametrize(
        "s, result",
        [("- - 1 2", "1 - 2"),
         ("+ 1 2 3", "1 + 2")]
    )
    def test_warning(self, s, result):
        with pytest.warns(UserWarning):
            assert Notations.to_infix_notation(s) == result
