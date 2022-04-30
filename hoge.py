import random

import click

from fizzbuzz import fizzbuzz as fb


@click.command()
@click.option(
    "--num",
    "-n",
    default=lambda: random.randint(1, 100),
    type=int,
    help="Number of loop",
)
def fizzbuzz(num: int):
    fb(num)


if __name__ == "__main__":
    fizzbuzz()
