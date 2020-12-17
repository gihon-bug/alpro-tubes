import sys
from enum import Enum
from cli.controller import ControllerCLI
from gui.controller import ControllerGUI
import modulfactory


class Mode(Enum):
    GUI = 1
    CLI = 2

def main( mode : Mode ):
    if mode == Mode.CLI:
        controller = ControllerCLI()
    elif mode == Mode.GUI:
        controller = ControllerGUI()
    controller.start( modulfactory.get_all_modul() )

    exit()

if "--cli" in sys.argv:
    main( Mode.CLI )
else:
    main( Mode.GUI )
