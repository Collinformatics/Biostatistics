import numpy as np
import pandas as pd





# ==================================== Set Parameters ====================================
roundVal = 3

# Colors:
greyDark = '\033[38;2;144;144;144m'
white = '\033[38;2;255;255;255m'
purple = '\033[38;2;189;22;255m'
magenta = '\033[38;2;255;0;128m'
pink = '\033[38;2;255;0;242m'
cyan = '\033[38;2;22;255;212m'
blue = '\033[38;5;51m'
green = '\033[38;2;5;232;49m'
greenLight = '\033[38;2;204;255;188m'
greenDark = '\033[38;2;30;121;13m'
yellow = '\033[38;2;255;217;24m'
orange = '\033[38;2;247;151;31m'
red = '\033[91m'
resetColor = '\033[0m'

# Print options
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', '{:,.3f}'.format)



# =================================== Define Functions ===================================
def describeSet(data, tag=''):
    print('=============================== Summarize Dataset '
          '===============================')
    print(f'Data: {purple}{tag}\n  {red}{", ".join(map(str, data))}{resetColor}\n')

    stats = {
        'N': len(data),
        'Mean': np.mean(data),
        'Median': np.median(data),
        'St Dev': np.std(data),
        'Variance': np.var(data),
        'Max Value': np.max(data),
        'Min Value': np.min(data)
    }

    print('Dataset Summary:')
    for key, value in stats.items():
        print(f'  {key}: {red}{round(value, roundVal)}{resetColor}')
    print('\n')

    return stats

def compairSets(data1, tag1, data2, tag2):
    print('=============================== Compare Datasets '
          '================================')
    print(f'Compair sets: {purple}{tag2}{resetColor} - {purple}{tag1}{resetColor}')
    for key in data1.keys():
        print(f'  Δ{key} = {round(data2[key], roundVal)} - '
              f'{round(data1[key], roundVal)} = '
              f'{red}{round(round(data2[key] - data1[key], roundVal), roundVal)}'
              f'{resetColor}')
    print('\n')

    
    