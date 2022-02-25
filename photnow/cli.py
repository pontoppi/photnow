"""
Usage:
    photnow <file> <x> <y> [--radius=<radius>]
    photnow <pattern> ...

Options:
    -h, --help                    Show this help
    --radius=<radius>             Extraction aperture radius [default: 10]
"""

from photnow import photnow
from docopt import docopt

def main():
    
    """Main CLI entrypoint."""
    arguments = docopt(__doc__, options_first=False)
    photnow.photnow(arguments)