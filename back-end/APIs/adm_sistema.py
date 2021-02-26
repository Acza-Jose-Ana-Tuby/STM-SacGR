from Models.adm_sistema import adm_sistema

import os
import sys
sys.path.append(os.path.realpath('.'))
from API_manager import manager


manager.create_api(adm_sistema, methods=['GET', 'POST', 'DELETE', 'PUT'])
