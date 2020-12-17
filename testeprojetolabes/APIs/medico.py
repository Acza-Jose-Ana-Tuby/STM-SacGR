from Models.medico import medico

import os
import sys
sys.path.append(os.path.realpath('.'))
from API_manager import manager


manager.create_api(medico, methods=['GET', 'POST', 'DELETE', 'PUT'])
