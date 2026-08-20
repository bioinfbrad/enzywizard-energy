from __future__ import annotations
from argparse import ArgumentParser,Namespace
import sys
from ..services.energy_service import run_energy_service


def add_energy_parser(parser:ArgumentParser) -> None:
    parser.add_argument("-i","--input_path", required=True, help="Path to the input cleaned protein structure file in CIF or PDB format.")
    parser.add_argument("-o","--output_dir", required=True, help="Path to the output directory for saving the JSON report.")
    parser.add_argument("--no_minimize_energy",action="store_false",dest="minimize_energy",help="Disable performing an energy minimization before energy evaluation (default: enabled).")
    parser.set_defaults(minimize_energy=True)
    parser.add_argument("--minimization_iteration",type=int,default=100,help="Maximum number of iterations for energy minimization (default: 100). A smaller value may result in energy values closer to the instantaneous (non-minimized) state.")
    parser.set_defaults(func=run_energy)


def run_energy(args: Namespace) -> None:
    success = run_energy_service(input_path=args.input_path,output_dir=args.output_dir,minimize_energy=args.minimize_energy,minimization_iteration=args.minimization_iteration)
    if not success:
        sys.exit(1)
