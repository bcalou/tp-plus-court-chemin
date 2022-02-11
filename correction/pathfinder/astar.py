from pathfinder.pathfinder import PathFinder
from pathfinder.city import City


class AStar(PathFinder):
    def __init__(self, graph, heuristics):
        super().__init__(graph)
        self._heuristics = heuristics

    def _get_city_distance_evaluation(self, city: City) -> int:
        """Add the heuristic to the distance for better evaluation"""

        return super()._get_city_distance_evaluation(city) \
          + self._heuristics[city]

    def _should_visit_city(self, city: City) -> bool:
        """Return true if the given city should be visited"""

        # Visit city unless an answer has already been found
        return self._cities[self._end]["distance"] == float('inf')
