# Opciones para el campo 'Tipo de identificacion'
CEDULA_CIUDADANIA = "CC"
REGISTRO_CIVIL = "RC"
NUIP = "NUIP"
TARJETA_IDENTIDAD = "TI"
TIPO_IDENTIFICACION_CHOICES = (
    (CEDULA_CIUDADANIA, "Cédula de ciudadanía"),
    (REGISTRO_CIVIL, "Registro civil"),
    (NUIP, "Número único de identificación personal"),
    (TARJETA_IDENTIDAD, "TARJETA_IDENTIDAD"),
)

# Opciones para el campo 'Parentesco'
PADRE = "PA"
MADRE = "MA"
CONYUGUE = "CO"
HERMANO = "HE"
CABEZA_FAMILIA = "CA"
ESPOSA = "ES"
HIJO = "HI"
YERNO = "YR"
NUERA = "NU"
SUEGRO = "SU"
SOBRINO = "SO"
CUÑADO = "CU"
TIO = "TI"
ABUELO = "AB"
PARENTESCO_CHOICES = (
    (PADRE, "Padre"),
    (MADRE, "Madre"),
    (CONYUGUE, "Cónyugue"),
    (HERMANO, "Hermano (a)"),
    (CABEZA_FAMILIA, "Cabeza de Familia"),
    (ESPOSA, "Esposa"),
    (HIJO, "Hijo (a)"),
    (YERNO, "Yerno (a)"),
    (NUERA, "Nuera"),
    (SUEGRO, "Suegro (a)"),
    (SOBRINO, "Sobrino (a)"),
    (CUÑADO, "Cuñado (a)"),
    (TIO, "Tío (a)"),
    (ABUELO, "Abuelo (a)"),
)

# Opciones para el campo 'Género'
MASCULINO = "M"
FEMENINO = "F"
GENERO_CHOICES = (
    (MASCULINO, "Masculino"),
    (FEMENINO, "Femenino"),
)

# Opciones para el campo 'Estado civil'
SOLTERO = "S"
CASADO = "C"
ESTADO_CIVIL_CHOICES = (
    (SOLTERO, "Soltero"),
    (CASADO, "Casado"),
)

# Opciones para el campo 'Escolaridad'
PRIMARIA = "PR"
SECUNDARIA = "SE"
UNIVERSITARIA = "UN"
NINGUNO = "NI"
ESCOLARIDAD_CHOICES = (
    (PRIMARIA, "Primaria"),
    (SECUNDARIA, "Secundaria"),
    (UNIVERSITARIA, "Universitaria"),
    (NINGUNO, "Ninguno")
    )
