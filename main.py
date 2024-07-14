import numpy as np
import json

def handler(event,  context):
    return json.dumps(np.ones((5,), dtype=int).tolist())
