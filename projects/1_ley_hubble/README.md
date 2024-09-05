# Proyecto 1: Ley de Hubble
Para comenzar a trabajr con modelos simples, vamos a partir con una regresión lineal y luego implementar otros modelos que veamos convenientes,

Estos son datos simulados por lo que es bueno para comenzar a trabajar, obtener resultados esperados y saltarse un poco la limpieza de datos que puede resultar más complicada que el mismo machine 

Origen del dataset: (Kaggle Ley Hubble)[https://www.kaggle.com/datasets/austinhinkel/hubble-law-astronomy-lab/data]

# La Ley de Hubble

La *Ley de Hubble* es una de las piezas fundamentales en la cosmología moderna, ya que describe la expansión del universo. La ley, propuesta por el astrónomo Edwin Hubble en 1929, establece una relación directa entre la **distancia a una galaxia** y la **velocidad a la que se aleja de nosotros** (debido a la expansión del universo). Esta relación se expresa matemáticamente como:

$$
v = H_0 \cdot d
$$

Donde:
- **$v$** es la **velocidad** a la que la galaxia se aleja de la Tierra (generalmente medida en km/s).
- **$d$** es la **distancia** a la galaxia (en megaparsecs, Mpc).
- **$H_0$** es la **constante de Hubble**, que mide la tasa de expansión del universo en unidades de km/s por Mpc.

## Explicación conceptual

La Ley de Hubble nos dice que las galaxias que están más lejos de nosotros se alejan a mayor velocidad. Esto implica que el universo está en expansión, un concepto clave para la teoría del Big Bang. Hubble descubrió esta relación observando el **corrimiento al rojo** ("redshift") en la luz de galaxias lejanas. Este corrimiento al rojo indica que la longitud de onda de la luz emitida por un objeto se alarga, lo que significa que el objeto se está alejando de nosotros.

## ¿Cómo se determina la Ley de Hubble?

Para determinar la Ley de Hubble, necesitamos conocer dos cosas:

1. **La velocidad de recesión de la galaxia**: Se determina a partir de su **redshift**. El redshift ($z$) es una medida de cómo ha cambiado la longitud de onda de la luz emitida por la galaxia, y puede relacionarse directamente con la velocidad a la que se aleja de nosotros usando la fórmula aproximada para velocidades pequeñas:

   $$
   v = z \cdot c
   $$

   Donde:
   - $v$ es la velocidad de recesión.
   - $z$ es el redshift.
   - $c$ es la velocidad de la luz (aproximadamente 300,000 km/s).

2. **La distancia a la galaxia**: En este caso, la distancia se puede calcular usando el **brillo de supernovas de tipo Ia**. Estas supernovas son conocidas como "velas estándar" porque tienen una **magnitud absoluta** casi constante. Si conocemos la magnitud aparente ($m$) de la supernova y su magnitud absoluta ($M$), podemos calcular la distancia mediante la **ecuación de la distancia en astronomía**:

   $$
   m - M = 5 \log_{10}(d) - 5
   $$

   Donde:
   - $m$ es la **magnitud aparente** observada.
   - $M$ es la **magnitud absoluta** conocida (para supernovas tipo Ia, $M \approx -19.3$).
   - $d$ es la **distancia** a la galaxia en parsecs.

   Despejando para la distancia $d$:

   $$
   d = 10^{\frac{m - M + 5}{5}}
   $$

## Inferencia de la Ley de Hubble a partir del dataset

El dataset simulado que tienes contiene dos columnas importantes:
1. **Magnitud aparente de las supernovas de tipo Ia**: Nos permitirá calcular la **distancia** a las galaxias utilizando la ecuación de la distancia mencionada anteriormente.
2. **Valores de redshift**: Nos permitirá calcular la **velocidad** de recesión de las galaxias.

### Procedimiento para inferir la Ley de Hubble:

1. **Calcular la distancia**: Utiliza la magnitud aparente de cada supernova en el dataset y la magnitud absoluta típica para supernovas de tipo Ia ($M = -19.3$) para calcular la distancia a la galaxia anfitriona.
2. **Calcular la velocidad de recesión**: Utiliza los valores de redshift ($z$) para calcular la velocidad a la que la galaxia se aleja de nosotros usando la fórmula $v = z \cdot c$.
3. **Realizar una regresión lineal**: Una vez que tengas las distancias y las velocidades, puedes hacer una regresión lineal para obtener la relación entre ambas. La pendiente de esta regresión te dará una estimación de la **constante de Hubble** ($H_0$).

