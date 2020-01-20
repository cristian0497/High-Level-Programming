#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    len_ma = len(m_a)
    len_mb = len(m_b)
    """ if lm_a or b different to list """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    """ if m_a or b is empty """
    if m_a == [] or m_a == [[]] or len_ma == 0:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]] or len_mb == 0:
        raise ValueError("m_b can't be empty")

    """ if any element of list is not int or float """
    for a in m_a:
        if type(a) != list:
            raise TypeError("m_a should contain only integers or floats")
        for num in a:
            if type(num) != int and type(num) != float:
                raise TypeError("m_a should contain only integers or floats")
            
