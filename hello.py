import argparse
from typing import Optional, Sequence

__version__ = "0.1.0"


def greet(name: str, punctuation: str = "!") -> str:
	name = name.strip()
	if not name:
		raise ValueError("name must not be empty")
	if punctuation not in {"!", ".", "?"}:
		raise ValueError("punctuation must be one of: !, ., ?")
	return f"Hello, {name}{punctuation}"


def main(argv: Optional[Sequence[str]] = None) -> int:
	parser = argparse.ArgumentParser(description="Print a friendly greeting.")
	parser.add_argument("--version", action="version", version=__version__)
	parser.add_argument("name", nargs="?", default="world", help="Name to greet")
	parser.add_argument(
		"--punctuation",
		choices=("!", ".", "?"),
		default="!",
		help="Punctuation to add to the greeting",
	)
	args = parser.parse_args(argv)

	try:
		print(greet(args.name, args.punctuation))
	except ValueError as error:
		parser.error(str(error))
	return 0


if __name__ == "__main__":
	main()