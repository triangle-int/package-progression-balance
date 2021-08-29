import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

"""
# Баланс прогрессии в :package: Package
Для того чтобы увидеть результат необходимо ввести исходные коэффиценты, которые будут подставлены в формулу:
"""

st.latex(r'''y = ax^k + bx^m * |\sin(cx^n)|''')

with st.form(key='constants_form'):
    '''
    ## Коэффиценты
    '''
    left_column, right_column = st.columns(2)

    left_column.write('Множители')
    a = left_column.number_input(label='a', value=1.0, step=0.1)
    b = left_column.number_input(label='b', value=1.0, step=0.1)
    c = left_column.number_input(label='c', value=1.0, step=0.1)
    
    right_column.write('Степени')
    k = right_column.number_input(label='k (Склон функции)', value=3.0, step=0.1)
    m = right_column.number_input(label='m', value=0.5, step=0.1)
    n = right_column.number_input(label='n', value=0.5, step=0.1)
    
    '''
    ## Дополнительные параметры
    '''
    max_level = st.number_input(label='Максимальный уровень', value=1, min_value=1)

    submit_button = st.form_submit_button(label='Смоделировать')

'''
Финальная формула будет выглядеть так:
'''

st.latex(fr'''y = {a}x^{{{k}}} + {b}x^{{{m}}} * |\sin({c}x^{{{n}}})|''')

if submit_button:
    levels = np.arange(max_level) + 1
    volume_to_up = a * np.power(levels, k) + b * np.power(levels, m) * np.sin(c * np.power(levels, n))

    df = pd.DataFrame({
        'Уровень': levels,
        'Объем для повышения уровня': volume_to_up,
    })

    st.dataframe(df.style.format('{:.0f}'))

    st.line_chart(df)