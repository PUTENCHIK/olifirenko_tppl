import pytest
from plib import Point, PointError


@pytest.fixture
def points() -> tuple:
    return Point(0, 0), Point(1, 2)


class TestPoint:

    def test_creation(self):
        Point(1, 1)
        
        with pytest.raises(PointError):
            Point(1, 1.5)
    
    def test_addition(self, points):
        a, b = points
        assert a + b == Point(1, 2)
        
    def test_addition_other(self, points):
        a, _ = points
        with pytest.raises(NotImplementedError):
            assert a + 1
        
    def test_subtract(self, points):
        a, b = points
        assert a - b == Point(-1, -2)
        
    def test_subtract_other(self, points):
        a, _ = points
        with pytest.raises(NotImplementedError):
            assert a - 1
        
    def test_eq(self, points):
        a, _ = points
        assert a == Point(0, 0)
        
    def test_eq_other(self, points):
        a, _ = points
        with pytest.raises(NotImplementedError):
            assert a == 1
        
    def test_distance(self, points):
        a, b = points
        assert a.distance(b) == 5**0.5
        
    def test_distance_other(self, points):
        a, _ = points
        with pytest.raises(NotImplementedError):
            assert a.distance(10)
        
    @pytest.mark.parametrize(
        "p1, p2, distance",
        [(Point(0, 0), Point(0, 0), 0),
         (Point(0, 0), Point(0, 10), 10),
         (Point(0, 0), Point(10, 0), 10),
         (Point(0, 0), Point(3, 4), 5),
         (Point(-5, 0), Point(5, 0), 10),
         (Point(0, 0), Point(10, 10), 14.14),]
    )
    def test_distance_all_axis(self, p1, p2, distance):
        assert p1.distance(p2) == pytest.approx(distance, 1e-1)
        
    def test_save_to_json(self):
        js = '{"x": 0, "y": 0}'
        p = Point(0, 0)
        assert p.to_json() == js
    
    def test_load_to_json(self):
        js = '{"x": 0, "y": 0}'
        p = Point.from_json(js)
        assert p == Point(0, 0)
        
    def test_is_center(self):
        a, b = Point(0, 0), Point(1, 1)
        assert a.is_center()
        assert not b.is_center()
