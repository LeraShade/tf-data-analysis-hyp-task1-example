import pandas as pd
import numpy as np


chat_id = 5105487223 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    data = pd.DataFrame({
        'group': ['X', 'Y'],
        'success': [x_success, y_success],
        'total': [x_cnt, y_cnt]
    })

    data['proportion'] = data['success'] / data['total']

    p_combined = data['success'].sum() / data['total'].sum()

    z_stat = (data['proportion'].diff()[-1]) / np.sqrt(
        p_combined * (1 - p_combined) * (1 / data['total']).sum()
    )

    p_value = 2 * (1 - 0.5 * (1 + math.erf(abs(z_stat) / np.sqrt(2))))

 
    alpha = 0.05
    return p_value < alpha
