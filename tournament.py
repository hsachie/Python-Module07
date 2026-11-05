from ex0 import FlameFactory, AquaFactory
from ex0.factory import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
	BattleStrategy,
	NormalStrategy,
	AggressiveStrategy,
	DefensiveStrategy,
	InvalidStrategyError,
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
	print("*** Tournament ***")
	print(f"{len(opponents)} opponents involved")
	try:
		for i in range(len(opponents)):
			for j in range(i + 1, len(opponents)):
				factory1, strategy1 = opponents[i]
				factory2, strategy2 = opponents[j]
				creature1 = factory1.create_base()
				creature2 = factory2.create_base()

				print()
				print("* Battle *")
				print(creature1.describe())
				print(" vs.")
				print(creature2.describe())
				print(" now fight!")
				strategy1.act(creature1)
				strategy2.act(creature2)
	except InvalidStrategyError as e:
		print(f"Battle error, aborting tournament: {e}")


def main() -> None:
	flame = FlameFactory()
	aqua = AquaFactory()
	healing = HealingCreatureFactory()
	transform = TransformCreatureFactory()

	normal = NormalStrategy()
	aggressive = AggressiveStrategy()
	defensive = DefensiveStrategy()

	print("Tournament 0 (basic)")
	print(" [ (Flameling+Normal), (Healing+Defensive) ]")
	battle([(flame, normal), (healing, defensive)])

	print()
	print("Tournament 1 (error)")
	print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
	battle([(flame, aggressive), (healing, defensive)])

	print()
	print("Tournament 2 (multiple)")
	print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
	battle([(aqua, normal), (healing, defensive), (transform, aggressive)])


if __name__ == "__main__":
	main()