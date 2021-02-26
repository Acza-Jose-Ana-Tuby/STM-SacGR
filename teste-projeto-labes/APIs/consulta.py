from Models.consulta import consulta

import os
import sys
sys.path.append(os.path.realpath('.'))
from API_manager import manager


manager.create_api(consulta, methods=['GET', 'POST', 'DELETE', 'PUT'])
