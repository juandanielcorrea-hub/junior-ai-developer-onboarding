El curso de Fundamentos de la Transformación de Datos de MongoDB University (cuyo núcleo es el Aggregation Framework) es una de las herramientas más potentes que puedes aprender. Cambia la forma en que interactúas con la base de datos, pasando de simples consultas a análisis de datos complejos y transformaciones profundas.

Aquí tienes un resumen estructurado, ideal para que lo uses como guía de estudio.

1. El Concepto Central: El Pipeline de Agregación
Piensa en el Aggregation Framework como una línea de ensamblaje en una fábrica. Los documentos entran por un extremo y pasan por diferentes "etapas" (stages). En cada etapa, los documentos se filtran, se modifican, se agrupan o se combinan, y el resultado se pasa a la siguiente etapa.

Sintaxis básica: db.coleccion.aggregate([ {etapa1}, {etapa2}, ... ])

2. Etapas Principales (Stages)
Estas son las operaciones fundamentales que debes memorizar:

Filtrado y Modelado Básico
$match: Filtra los documentos. Es exactamente igual que un find(). Regla de oro: Úsalo lo antes posible en tu pipeline para reducir la cantidad de datos y aprovechar los índices de la base de datos.

$project: Modifica la estructura del documento. Sirve para incluir (1) o excluir (0) campos, y también para crear campos nuevos asignándoles valores de otros campos.

$set / $addFields: Agrega nuevos campos a los documentos o reescribe campos existentes. (A diferencia de $project, mantiene los campos originales que no mencionaste).

$unset: Elimina campos específicos de los documentos.

Agrupación de Datos
$group: Agrupa documentos por un campo o expresión específica (este será su _id). Es la base para sacar métricas.

Acumuladores comunes: Se usan dentro de $group para hacer cálculos matemáticos o de arreglos: $sum (para contar o sumar totales), $avg (promedio), $max, $min, $push (crea un array con valores, permite duplicados), $addToSet (crea un array, no permite duplicados).

Orden y Paginación
$sort: Ordena los documentos ascendente (1) o descendentemente (-1).

$limit: Restringe el número de documentos que pasan a la siguiente etapa.

$skip: Salta un número determinado de documentos. (Nota: Para paginación, el orden suele ser $sort -> $skip -> $limit).

3. Manejo Avanzado de Arrays y Relaciones
Descomposición de Arrays
$unwind: Toma un array dentro de un documento y crea un documento nuevo por cada elemento de ese array.

Ejemplo: Si un documento de "Usuario" tiene un array de 3 "Compras", $unwind generará 3 documentos separados de "Usuario", cada uno con una compra individual.

Uniones (Joins)
$lookup: Permite unir datos de diferentes colecciones (equivalente a un LEFT OUTER JOIN en SQL).

Requiere 4 parámetros:

from: La colección a unir.

localField: El campo de tu colección actual.

foreignField: El campo de la colección externa.

as: El nombre del nuevo array donde se guardarán los resultados emparejados.

4. Mejores Prácticas y Rendimiento (¡Súper importante para el examen!)
Para asegurar que tus pipelines sean eficientes, MongoDB University hace mucho énfasis en lo siguiente:

Uso de Índices: Solo las etapas $match y $sort pueden usar índices, y solo si se encuentran al principio del pipeline. Una vez que alteras los datos con un $project, $group o $unwind, los índices originales ya no sirven en las siguientes etapas.

Filtrar temprano: Mientras menos datos pasen por el pipeline, más rápido será. Pon tus $match y $limit al inicio siempre que sea lógicamente posible.

Límites de Memoria: Cada etapa del pipeline tiene un límite de RAM de 100 MB. Si superas este límite (por ejemplo, ordenando millones de registros sin índice), la consulta fallará. Para evitarlo, se debe usar la opción { allowDiskUse: true }, lo que escribe datos temporales en el disco, aunque lo hace más lento.