def volt(V, C_imp):
    CD = ((36.892 * (V**5)) - (72.053*(V**4)) + ((54.77)*(V**3))- ((20.409)*(V**2)) + (4.2829*V) - 0.0635 + C_imp)
    return CD