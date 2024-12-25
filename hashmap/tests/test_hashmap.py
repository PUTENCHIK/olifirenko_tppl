import pytest
from hashmap import Iloc, Ploc, HashMap, InvalidTokenOrder


@pytest.fixture()
def map1(scope="function") -> HashMap:
    return HashMap({
        "value1": 1,
        "value2": 2,
        "value3": 3,
        "1": 10,
        "2": 20,
        "3": 30,
        "1, 5": 100,
        "5, 5": 200,
        "10, 5": 300,
    })


@pytest.fixture()
def map2(scope="function") -> HashMap:
    return HashMap({
        "value1": 1,
        "value2": 2,
        "value3": 3,
        "1": 10,
        "2": 20,
        "3": 30,
        "(1, 5)": 100,
        "(5, 5)": 200,
        "(10, 5)": 300,
        "(1, 5, 3)": 400,
        "(5, 5, 4)": 500,
        "(10, 5, 5)": 600,
    })


class TestHashMap:

    def test_init(self):
        map = HashMap()
        assert map == {}
    
    def test_properties(self, map1):
        assert isinstance(map1.iloc, Iloc)
        assert isinstance(map1.ploc, Ploc)
    
    def test_set_value(self, map1):
        map1["new1"] = 1
        map1["new2"] = "2"
        map1["new3"] = [3]
        
        assert map1["new1"] == 1
        assert map1["new2"] == "2"
        assert map1["new3"] == [3]


class TestIloc:
    
    def test_getitem(self, map1):
        assert map1.iloc[0] == 10
        assert map1.iloc[2] == 300
        assert map1.iloc[5] == 200
        assert map1.iloc[8] == 3

    def test_errors(self, map1):
        with pytest.raises(AttributeError):
            map1.iloc["string"]

        with pytest.raises(KeyError):
            map1.iloc[20]


class TestPloc:

    def test_getitem(self, map2):
        assert map2.ploc[">=1"] == {'1': 10, '2': 20, '3': 30}
        assert map2.ploc["<3"] == {'1': 10, '2': 20}
        assert map2.ploc[">0, >0"] == {'(1, 5)': 100, '(5, 5)': 200, '(10, 5)': 300}
        assert map2.ploc[">=10, >0"]  == {'(10, 5)': 300}
        assert map2.ploc["<5, >=5, >=3"] == {'(1, 5, 3)': 400}
    
    def test_bad_condition(self, map2):
        with pytest.raises(InvalidTokenOrder):
            map2.ploc[",>1"]

    def test_bad_getitem(self, map1):
        with pytest.raises(AttributeError):
            map1.ploc[0]



