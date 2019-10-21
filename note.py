import argparse


def main(mark: float, source_max: int, dest_max: int):
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('mark', type=float,
                        help='The mark assigned to you.')
    parser.add_argument('source_max', type=float,
                        help='The maximal value your mark could have taken.')
    parser.add_argument('dest_max', type=float,
                        help="The maximal value your mark could have taken in your destination domain.")
    args = parser.parse_args()

    note(
        mark=args.mark,
        source_max=args.source_max,
        dest_max=args.dest_max
    )


def note(mark: float, source_max: float, dest_max: float) -> None:
    print((mark * dest_max) / source_max)


if __name__ == '__main__':
    main()
