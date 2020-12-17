from Models.paciente import paciente

import os
import sys
sys.path.append(os.path.realpath('.'))
from API_manager import manager


manager.create_api(paciente, methods=['GET', 'POST', 'DELETE', 'PUT'])
