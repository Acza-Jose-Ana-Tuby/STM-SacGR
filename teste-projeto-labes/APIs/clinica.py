from Models.clinica import clinica

import os
import sys
sys.path.append(os.path.realpath('.'))
from API_manager import manager


manager.create_api(clinica, methods=['GET', 'POST', 'DELETE', 'PUT'])
