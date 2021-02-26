from Models.politica_agendamento import politica_agendamento

import os
import sys
sys.path.append(os.path.realpath('.'))
from API_manager import manager

manager.create_api(politica_agendamento, methods=['GET', 'POST', 'DELETE', 'PUT'])
