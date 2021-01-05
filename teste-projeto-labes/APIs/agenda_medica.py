from Models.agenda_medica import agenda_medica

import os
import sys
sys.path.append(os.path.realpath('.'))
from API_manager import manager


manager.create_api(agenda_medica, methods=['GET', 'POST', 'DELETE', 'PUT'])
