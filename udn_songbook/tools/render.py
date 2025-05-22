#!/usr/bin/env python
"""Render a songbook from a list of content."""
# steps
# 1. Build book via udn-songbook
# 2. Batch index
# 3. Append pages

import argparse
import sys
from datetime import datetime
from pathlib import Path

from loguru import logger

from udn_songbook import SongBook
from udn_songbook.utils import renderer

DATEFMT = "%Y-%m-%d.%H%M%S"
NOW = datetime.now()


def parse_cmdline(argv: list[str] = sys.argv[1:]) -> argparse.Namespace:
    """Process commandline arguments."""

    parser = argparse.ArgumentParser(
        description="Publish a PDF songbook from a series of inputs",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "sources",
        nargs="+",
        type=Path,
        help="one or more input sources (directories or files) "
        "for UDN-formatted content",
    )

    parser.add_argument(
        "-p",
        "--profile",
        help="Book profile to generate, these are defined in `defaults.toml` "
        "in the udn-songbook installation dir, or in your songbook source dirs.",
    )

    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path(f"songbook-{NOW.strftime(DATEFMT)}.pdf"),
        help="output filename for generated book, can be an absolute path. "
        "Any parent directories will be created, if possible",
    )

    parser.add_argument(
        "-t",
        "--title",
        default="Songbook",
        help="title for songbook, will be on index page.",
    )

    parser.add_argument(
        "-b",
        "--batch",
        type=int,
        default=80,
        help="Number of index entries per index page.",
    )

    parser.add_argument(
        "--templates", type=Path, help="Directory containing custom jinja2 templates."
    )

    args = parser.parse_args(argv)

    logger.debug("Ignoring any sources that do not exist.")
    args.sources = [s for s in args.sources if s.exists()]

    return args


def main():
    opts = parse_cmdline(sys.argv[1:])

    book = SongBook(inputs=opts.sources)

    opts.output.parent.mkdir(exist_ok=True, parents=True)

    jinja_env = renderer()

    # load the index template
    idx_tpl = jinja_env.get_template(book.index_template)
    print(idx_tpl)

    print(book, len(book.index))
    print(book.settings.as_dict())


if __name__ == "__main__":
    main()
