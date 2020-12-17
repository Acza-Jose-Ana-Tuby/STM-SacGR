from Models.adm_clinica import adm_clinica

import os
import sys
sys.path.append(os.path.realpath('.'))
from API_manager import manager


manager.create_api(adm_clinica, methods=['GET', 'POST', 'DELETE', 'PUT'])
