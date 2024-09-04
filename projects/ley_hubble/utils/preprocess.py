
def aDistanciaVelocidad(data):
    """
    Calcula las distancias a supernovas tipo Ia y sus velocidades de recesión a partir de su magnitud aparente y redshift.

    Esta función toma un DataFrame con los datos de las supernovas, incluyendo la magnitud aparente y el redshift, 
    y calcula lo siguiente:
    1. La distancia a cada supernova en megaparsecs (Mpc), usando la magnitud absoluta predeterminada de -19.3.
    2. La velocidad de recesión de las supernovas en km/s, utilizando la ley de Hubble.

    Args:
    data (pandas.DataFrame): DataFrame que contiene las columnas 'apparent_magnitude' (magnitud aparente) y 
                             'redshift' (corrimiento al rojo).

    Returns:
    tuple: Un par de arrays (X, y) donde:
           - X (numpy.ndarray): Array 1D de distancias en megaparsecs.
           - y (numpy.ndarray): Array 1D de velocidades de recesión en km/s.
    """

    # Definir la magnitud absoluta de las supernovas tipo Ia
    M_absoluta = -19.3

    # Calcular las distancias (en parsecs)
    data['distancia'] = 10 ** ((data['apparent_magnitude'] - M_absoluta + 5) / 5)

    # se pasa a Mega parsec
    data['distancia'] = data['distancia'] / 10**6

    # Calcular las velocidades de recesión (en km/s)
    velocidad_luz = 300000  # km/s
    data['velocidad'] = data['redshift'] * velocidad_luz

    # Preparar los datos para la regresión lineal
    X = data['distancia'].values.reshape(-1, 1)  # Distancia
    y = data['velocidad'].values  # Velocidad

    return X, y