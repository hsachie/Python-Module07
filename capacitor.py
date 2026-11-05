from ex0.factory import CreatureFactory
from ex0.creature import Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capability import HealCapability, TransformCapability


def test_healing(factory: CreatureFactory) -> None:
	print("Testing Creature with healing capability")

	print(" base:")
	base = factory.create_base()
	print(base.describe())
	print(base.attack())
	if isinstance(base, HealCapability):
		print(base.heal())

	print(" evolved:")
	evolved = factory.create_evolved()
	print(evolved.describe())
	print(evolved.attack())
	if isinstance(evolved, HealCapability):
		print(evolved.heal())

def test_transform(factory: CreatureFactory) -> None:
	print("Testing Creature with transform capability")

	print(" base:")
	base = factory.create_base()
	print(base.describe())
	print(base.attack())
	if isinstance(base, TransformCapability):
		print(base.transform())
		print(base.attack())
		print(base.revert())

	print(" evolved:")
	evolved = factory.create_evolved()
	print(evolved.describe())
	print(evolved.attack())
	if isinstance(evolved, TransformCapability):
		print(evolved.transform())
		print(evolved.attack())
		print(evolved.revert())



def main() -> None:
	test_healing(HealingCreatureFactory())
	print()
	test_transform(TransformCreatureFactory())


if __name__ == "__main__":
	main()