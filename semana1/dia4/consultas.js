// QUERY 1: Búsqueda simple a partir de una fecha ($gte)
// Obtiene todos los documentos creados desde el 1 de enero de 2024.

db.ventas.find({
    fechaCreacion: { 
        $gte: ISODate("2024-01-01T00:00:00.000Z") 
    }
});

// QUERY 2: Búsqueda simple en un rango de fechas ($gte y $lte)
// Obtiene documentos creados estrictamente durante el mes de junio de 2024.

db.ventas.find({
    fechaCreacion: {
        $gte: ISODate("2024-06-01T00:00:00.000Z"),
        $lte: ISODate("2024-06-30T23:59:59.999Z")
    }
});

// QUERY 3: Aggregation Pipeline - $match con rango de fechas
// Filtra la colección usando el pipeline de agregación para el año 2023.

db.ventas.aggregate([
    {
        $match: {
            fechaCreacion: {
                $gte: ISODate("2023-01-01T00:00:00.000Z"),
                $lte: ISODate("2023-12-31T23:59:59.999Z")
            }
        }
    }
]);

// QUERY 4: Aggregation Pipeline - $match de fecha + $group
// Filtra por fecha y luego agrupa para contar el total de documentos en ese periodo.

db.ventas.aggregate([
    {
        $match: {
            fechaCreacion: { 
                $gte: ISODate("2024-01-01T00:00:00.000Z") 
            }
        }
    },
    {
        $group: {
            _id: null,
            totalVentasPeriodo: { $sum: 1 }
        }
    }
]);

// QUERY 5: Aggregation Pipeline - $match + extracción de mes en $project
// Filtra un rango de fechas y usa $project para extraer únicamente el mes usando $month.

db.ventas.aggregate([
    {
        $match: {
            fechaCreacion: {
                $gte: ISODate("2024-01-01T00:00:00.000Z"),
                $lte: ISODate("2024-12-31T23:59:59.999Z")
            }
        }
    },
    {
        $project: {
            _id: 0,
            monto: 1,
            mesOperacion: { $month: "$fechaCreacion" }
        }
    }
]);

// QUERY 6: Aggregation Pipeline Completo - $match + $group (por mes) + $sort
// Filtra a partir de una fecha, agrupa calculando el total de ventas por mes, y ordena cronológicamente.

db.ventas.aggregate([
    {
        $match: {
            fechaCreacion: { 
                $gte: ISODate("2023-01-01T00:00:00.000Z") 
            }
        }
    },
    {
        $group: {
            _id: { $month: "$fechaCreacion" },
            cantidadOperaciones: { $sum: 1 },
            ingresoTotalMes: { $sum: "$monto" }
        }
    },
    {
        $sort: { "_id": 1 }
    }
]);