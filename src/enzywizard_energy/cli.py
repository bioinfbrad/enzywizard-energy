from __future__ import annotations

import argparse

from .commands.energy import add_energy_parser


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="enzywizard-energy",
        description="EnzyWizard-Energy: Calculate molecular mechanics energy terms from a cleaned protein structure and generate a detailed JSON report."
    )
    add_energy_parser(parser)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)