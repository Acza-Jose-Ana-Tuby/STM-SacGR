from Models.clinica_possui_medico import clinica_possui_medico

import os
import sys
sys.path.append(os.path.realpath('.'))
from API_manager import manager


manager.create_api(clinica_possui_medico, methods=['GET', 'POST', 'DELETE', 'PUT'])
