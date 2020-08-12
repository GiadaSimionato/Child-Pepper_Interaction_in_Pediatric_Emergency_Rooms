import os, sys

pdir = os.getenv('MODIM_HOME')
sys.path.append(pdir + '/src/GUI')

from ws_client import *
import ws_client

from interactions import *

if __name__ == '__main__':
    # Connection to local MODIM server
    mws = ModimWSClient()
    mws.setDemoPathAuto(__file__)
    
    #mws.run_interaction(detection)

    mws.run_interaction(welcome)

    mws.run_interaction(getemotion)

    mws.run_interaction(menu)