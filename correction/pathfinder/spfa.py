from pathfinder.pathfinder import PathFinder
from pathfinder.city import City


class SPFA(PathFinder):
    def _get_next_city_to_visit(self) -> City:
        """Get the next city in the list"""

        # No particular order in SPFA, just take the first
        return self._cities_to_visit[0]

    def _should_visit_city(self, city: City) -> bool:
        """Return true if the given city should be visited"""

        # In SPFA, always visit a city, we may decrease the cost later
        return True