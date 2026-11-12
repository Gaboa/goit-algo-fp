from heapq import heappop, heappush
from math import inf
from typing import TypedDict

WeightedGraph = dict[str, dict[str, int | float]]
class RouteResult(TypedDict):
	distance: float
	path: list[str]


def dijkstra(
	graph: WeightedGraph,
	start: str,
) -> dict[str, RouteResult]:
	vertices = set(graph)
	for neighbors in graph.values():
		vertices.update(neighbors)

	result: dict[str, RouteResult] = {
		vertex: {"distance": inf, "path": []} for vertex in vertices
	}
	result[start] = {"distance": 0, "path": [start]}
	queue: list[tuple[float, str]] = [(0, start)]

	while queue:
		current_distance, current_vertex = heappop(queue)
		if current_distance > result[current_vertex]["distance"]:
			continue

		for neighbor, weight in graph.get(current_vertex, {}).items():
			candidate_distance = current_distance + float(weight)
			if candidate_distance < result[neighbor]["distance"]:
				result[neighbor] = {
					"distance": candidate_distance,
					"path": result[current_vertex]["path"] + [neighbor],
				}
				heappush(queue, (candidate_distance, neighbor))

	return result


def main():
	graph: WeightedGraph = {
		"A": {"B": 4, "C": 1},
		"B": {"A": 4, "C": 2, "D": 5},
		"C": {"A": 1, "B": 2, "D": 8, "E": 10},
		"D": {"B": 5, "C": 8, "E": 2},
		"E": {"C": 10, "D": 2},
	}
	start = "A"
	result = dijkstra(graph, start)

	print(f"Найкоротші шляхи від {start}:")
	for target in sorted(result):
		distance = result[target]["distance"]
		path = result[target]["path"]
		print(
			f"{start} -> {target}: відстань {distance:g}; "
			f"шлях {' -> '.join(path)}"
		)


if __name__ == "__main__":
	main()
