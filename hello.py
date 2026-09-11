import argparse
from typing import Optional, Sequence


def greet(name: str) -> str:
	name = name.strip()
	if not name:
		raise ValueError("name must not be empty")
	return f"Hello, {name}!"


def main(argv: Optional[Sequence[str]] = None) -> int:
	parser = argparse.ArgumentParser(description="Print a friendly greeting.")
	parser.add_argument("name", nargs="?", default="world", help="Name to greet")
	args = parser.parse_args(argv)

	try:
		print(greet(args.name))
	except ValueError as error:
		parser.error(str(error))
	return 0


if __name__ == "__main__":
	main()