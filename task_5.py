from collections import deque

import matplotlib.pyplot as plt
import networkx as nx

from task_4 import Node, build_heap_tree


def depth_first_traversal(root: Node | None) -> list[Node]:
	if root is None:
		return []

	visited = []
	stack = [root]
	while stack:
		node = stack.pop()
		visited.append(node)
		if node.right is not None:
			stack.append(node.right)
		if node.left is not None:
			stack.append(node.left)
	return visited


def breadth_first_traversal(root: Node | None) -> list[Node]:
	if root is None:
		return []

	visited = []
	queue = deque([root])
	while queue:
		node = queue.popleft()
		visited.append(node)
		if node.left is not None:
			queue.append(node.left)
		if node.right is not None:
			queue.append(node.right)
	return visited


def traversal_colors(nodes: list[Node]) -> dict[str, str]:
	start_color = (22, 50, 79)
	end_color = (255, 255, 200)
	colors = {}

	for index, node in enumerate(nodes):
		progress = index / max(len(nodes) - 1, 1)
		red = round(start_color[0] + (end_color[0] - start_color[0]) * progress)
		green = round(start_color[1] + (end_color[1] - start_color[1]) * progress)
		blue = round(start_color[2] + (end_color[2] - start_color[2]) * progress)
		colors[node.id] = f"#{red:02X}{green:02X}{blue:02X}"

	return colors


def build_graph_layout(root: Node):
	tree = nx.DiGraph()
	positions = {}
	stack = [(root, 0.0, 0.0, 1)]

	while stack:
		node, x, y, layer = stack.pop()
		tree.add_node(node.id, label=node.val)
		positions[node.id] = (x, y)

		if node.left is not None:
			left_x = x - 1 / 2**layer
			tree.add_edge(node.id, node.left.id)
			stack.append((node.left, left_x, y - 1, layer + 1))
		if node.right is not None:
			right_x = x + 1 / 2**layer
			tree.add_edge(node.id, node.right.id)
			stack.append((node.right, right_x, y - 1, layer + 1))

	return tree, positions


def draw_traversal(ax, tree, positions, order, title):
	colors = traversal_colors(order)
	visit_order = {node.id: index + 1 for index, node in enumerate(order)}
	labels = {
		node.id: f"{node.val}\n\n{visit_order[node.id]}" for node in order
	}

	nx.draw_networkx(
		tree,
		pos=positions,
		ax=ax,
		labels=labels,
		node_color=[colors[node_id] for node_id in tree.nodes],
		node_size=1800,
		font_size=9,
	)
	ax.set_title(title)
	ax.axis("off")


def visualize_traversals(root: Node | None) -> None:
	if root is None:
		return

	tree, positions = build_graph_layout(root)
	dfs_order = depth_first_traversal(root)
	bfs_order = breadth_first_traversal(root)

	figure, axes = plt.subplots(1, 2, figsize=(14, 7))
	draw_traversal(axes[0], tree, positions, dfs_order, "Обхід у глибину (стек)")
	draw_traversal(axes[1], tree, positions, bfs_order, "Обхід у ширину (черга)")
	figure.tight_layout()
	plt.show()


def main() -> None:
	heap = [0, 4, 1, 5, 10, 3]
	root = build_heap_tree(heap)
	visualize_traversals(root)


if __name__ == "__main__":
	main()
