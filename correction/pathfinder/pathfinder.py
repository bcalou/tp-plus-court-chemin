from typing import TypedDict
from pathfinder.city import City


class Path(TypedDict):
    total: float
    steps: list[City]


class PathFinder:
    def __init__(self, graph):
        self._graph = graph

    def get_shortest_path(self, start: City, end: City) -> Path:
        """Get the shortest route between 2 cities"""
        self._start = start
        self._end = end
        self._cities = self._init_cities()

        # At the start, we can only visit the city from which we come
        self._cities_to_visit: list = [start]

        # While we still have cities to visit
        while len(self._cities_to_visit):

            print("We must visit", self._cities_to_visit)

            # Visit the closest city available
            self._visit_city(self._get_next_city_to_visit())

        return self._get_formatted_path()

    def _init_cities(self):
        """Get the cities with initial distances from the graph"""
        cities = {}

        # Each city has an infinite distance at the start
        for city in self._graph.keys():
            cities[city] = {
              "distance": float("inf")
            }

        # Only the starting city has a distance of zero
        cities[self._start]["distance"] = 0

        return cities

    def _get_next_city_to_visit(self) -> City:
        """Get the closest city"""
        return min(
            self._cities_to_visit,
            key=self._get_city_distance_evaluation
        )

    def _get_city_distance_evaluation(self, city: City) -> int:
        """Get the city distance"""

        return self._cities[city]["distance"]

    def _visit_city(self, city: City) -> None:
        """Try the routes connected to this city"""
        if self._should_visit_city(city):

            print("___\nNow visiting:", city.name)

            # Try each city connected to the current one
            for connected_city in self._graph[city]:
                self._test_route(city, connected_city)

        # Mark the city as visited and remove from the visit list
        self._cities_to_visit.remove(city)

    def _should_visit_city(self, city: City) -> bool:
        """Return True if the given city should be visited"""
        destination_distance = self._cities[self._end]["distance"]

        # Skip cities that are farther than the destination itself
        return self._cities[city]["distance"] < destination_distance

    def _test_route(self, current_city: City, connected_city: City) -> None:
        """Test the route between two cities"""

        # The distance to the connected city is the distance of the current
        # city + the cost for this connection
        connected_city_distance = self._cities[current_city]["distance"] \
            + self._graph[current_city][connected_city]

        # Update the distance if it's better than what we already have
        if self._cities[connected_city]["distance"] > connected_city_distance \
        and self._cities[self._end]["distance"] > connected_city_distance:
            print("New route to", connected_city, "found ")
            print(connected_city_distance, "from", current_city)
            self._cities[connected_city]["distance"] = connected_city_distance

            # Remember where we come from
            self._cities[connected_city]["from"] = current_city

            # Add connected city to the list of cities to visit
            if connected_city not in self._cities_to_visit:
                self._cities_to_visit.append(connected_city)

    def _get_formatted_path(self) -> Path:
        """Convert the cities object to a formatted path answer"""

        path: Path = {
            "total": self._cities[self._end]["distance"],
            "steps": [self._end]  # We only know the last step at the moment
        }

        previous_step = self._cities[self._end]

        # While we come from somewhere...
        while "from" in previous_step:

            # Insert where we come from at the beginning of the steps array
            path["steps"].insert(0, previous_step['from'])

            # Rewind the steps
            previous_step = self._cities[previous_step["from"]]

        return path
