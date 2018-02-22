import click


@click.command()
@click.argument('mark', type=float)
@click.argument('source_max', type=int)
@click.argument('dest_max', type=int)
def mark(mark: float, source_max: int, dest_max: int):
	print((mark * dest_max) / source_max)



if __name__ == '__main__':
	mark()
