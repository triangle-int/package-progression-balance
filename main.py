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
    a = left_column.number_input(label='a (Амплитуда главной кривой)', value=2.0, step=0.1)
    b = left_column.number_input(label='b (Амплитуда волн)', value=40.0, step=0.1)
    c = left_column.number_input(label='c (Период волн)', value=0.2, step=0.1)
    
    right_column.write('Степени')
    k = right_column.number_input(label='k (Склон главной кривой)', value=3.0, step=0.1)
    m = right_column.number_input(label='m (Растяжение амплитуды волн со временем)', value=1.5, step=0.1)
    n = right_column.number_input(label='n (Растяжение периода волн со временем)', value=1.5, step=0.1)
    
    '''
    ## Дополнительные параметры
    '''
    max_level = st.number_input(label='Максимальный уровень', value=1, min_value=1)
    smoothed = st.checkbox('Сглаженная кривая')

    submit_button = st.form_submit_button(label='Смоделировать')

'''
Финальная формула будет выглядеть так:
'''

st.latex(fr'''y = {a}x^{{{k}}} + {b}x^{{{m}}} * |\sin({c}x^{{{n}}})|''')

def volumeToUp(x):
    return a * np.power(x, k) + b * np.power(x, m) * np.absolute(np.sin(c * np.power(x, n)))


if submit_button:
    levels = np.arange(max_level) + 1
    volume_to_up = volumeToUp(levels)

    df = pd.DataFrame({
        'Уровень': levels,
        'Объем для повышения уровня': volume_to_up,
    }, index=levels)

    if smoothed:
        levels_smoothed = np.arange(1, max_level + 0.05, step=0.05)
        volume_to_up_smoothed = volumeToUp(levels_smoothed)
        volume_to_up_main_curve_smooothed = a * np.power(levels_smoothed, k)

        chart_df = pd.DataFrame({
            'Объем для повышения уровня': volume_to_up_smoothed,
            'Без волн': volume_to_up_main_curve_smooothed,
        }, index=levels_smoothed)
    else:
        volume_to_up_main_curve = a * np.power(levels, k)

        chart_df = pd.DataFrame({
            'Объем для повышения уровня': volume_to_up,
            'Без волн': volume_to_up_main_curve,
        }, index=levels)

    

    st.dataframe(df.style.format('{:.0f}'))

    st.line_chart(chart_df)