from Models.atendente import atendente

import os
import sys
sys.path.append(os.path.realpath('.'))
from API_manager import manager


manager.create_api(atendente, methods=['GET', 'POST', 'DELETE', 'PUT'])
