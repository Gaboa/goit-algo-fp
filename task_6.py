items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(foods: dict[str, dict[str, int]], budget: int) -> list[str]:
    def calorie_cost_ratio(name: str) -> float:
        food = foods[name]
        return food["calories"] / food["cost"]

    food_names = sorted(foods, key=calorie_cost_ratio, reverse=True)
    selected = []
    remaining_budget = budget

    for name in food_names:
        cost = foods[name]["cost"]
        if cost <= remaining_budget:
            selected.append(name)
            remaining_budget -= cost

    return selected


def dynamic_programming(
    foods: dict[str, dict[str, int]], budget: int
) -> list[str]:
    food_names = list(foods)
    calories_by_budget = [
        [0] * (budget + 1) for _ in range(len(food_names) + 1)
    ]

    for index, name in enumerate(food_names, start=1):
        cost = foods[name]["cost"]
        calories = foods[name]["calories"]
        for current_budget in range(budget + 1):
            calories_by_budget[index][current_budget] = calories_by_budget[
                index - 1
            ][current_budget]
            if cost <= current_budget:
                calories_by_budget[index][current_budget] = max(
                    calories_by_budget[index][current_budget],
                    calories_by_budget[index - 1][current_budget - cost]
                    + calories,
                )

    selected = []
    remaining_budget = budget

    for index in range(len(food_names), 0, -1):
        if calories_by_budget[index][remaining_budget] != calories_by_budget[
            index - 1
        ][remaining_budget]:
            name = food_names[index - 1]
            selected.append(name)
            remaining_budget -= foods[name]["cost"]

    return list(selected)


def main() -> None:
    budget = 100
    for algorithm in (greedy_algorithm, dynamic_programming):
        selected = algorithm(items, budget)
        total_cost = sum(items[name]["cost"] for name in selected)
        total_calories = sum(items[name]["calories"] for name in selected)
        print(
            f"{algorithm.__name__}: {', '.join(selected)} "
            f"(вартість: {total_cost}, калорійність: {total_calories})"
        )


if __name__ == "__main__":
    main()
