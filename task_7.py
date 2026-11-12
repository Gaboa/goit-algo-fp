import random


def analytical_probabilities() -> dict[int, float]:
	return {
		total: (6 - abs(7 - total)) / 36
		for total in range(2, 13)
	}


def simulate_dice_rolls(
	number_of_rolls: int = 100_000
) -> tuple[dict[int, int], dict[int, float]]:
	generator = random.Random(42)
	counts = dict.fromkeys(range(2, 13), 0)
	for _ in range(number_of_rolls):
		total = generator.randint(1, 6) + generator.randint(1, 6)
		counts[total] += 1

	probabilities = {
		total: count / number_of_rolls
		for total, count in counts.items()
	}
	return counts, probabilities


def print_results(
	counts: dict[int, int],
	simulated: dict[int, float],
	analytical: dict[int, float],
) -> None:
	print(
		f"{'Сума':>4} {'Кількість':>12} {'Монте-Карло':>14} {'Аналітична':>14}"
	)
	for total in range(2, 13):
		print(
			f"{total:>4} {counts[total]:>12} "
			f"{simulated[total]:>13.2%} "
			f"{analytical[total]:>13.2%} "
		)

def main() -> None:
	number_of_rolls = 100_000
	counts, simulated = simulate_dice_rolls(number_of_rolls)
	analytical = analytical_probabilities()

	print(f"Кількість симуляцій: {number_of_rolls}")
	print_results(counts, simulated, analytical)


if __name__ == "__main__":
	main()
