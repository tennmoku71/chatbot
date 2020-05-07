import os
import sys
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

os.chdir('chatbotweb/')
from chatbotweb import server
server.run()
