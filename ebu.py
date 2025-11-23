#!/usr/bin/env python3
import argparse



def get_args():
	parser = argparse.ArgumentParser()

	parser.add_argument("link", help="The main URL of the blog")
	parser.add_argument("-l", "--listing", nargs="+", metavar="SELECTOR", help="CSS selectors for listing extraction")
	parser.add_argument("-c", "--content", nargs="+", metavar="SELECTOR", help="CSS selectors for content extraction")

	parser.add_argument("-t", "--title", help="Optional title", default=None)
	parser.add_argument("-d", "--description", help="Optional description", default=None)

	return parser.parse_args()


def main():
	args = get_args()
	print(args)


if __name__ == '__main__':
	main()
