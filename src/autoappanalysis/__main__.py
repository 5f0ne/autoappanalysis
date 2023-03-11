import sys
import json
import argparse

from autoappanalysis.model.Vm import Vm
from autoappanalysis.gui.Gui import Gui

def main(args_=None):
    """The main routine."""
    if args_ is None:
        args_ = sys.argv[1:]

    parser = argparse.ArgumentParser()
   
    parser.add_argument("--config", "-c", type=str, required=True, help="Path to config file")
    args = parser.parse_args()

    f = open(args.config)
    c = json.load(f)
 
    gui = Gui(c["vm"], c["user"], c["pw"], c["input"], c["output"], c["outputHost"], c["snapshot"])
    gui.start()

if __name__ == "__main__":
    sys.exit(main())

