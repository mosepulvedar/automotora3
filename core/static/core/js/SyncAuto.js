class SyncAuto {

    constructor() {
        this.conexion  = new Conexion().conectar();
        this.urlAuto = "/api/listado-autos";
    }

    SyncAutos() {
        var conn = this.conexion;
        return fetch(this.urlAuto)
        .then(function(data){
            return data.json();
        })
        .then(function(data) {
            console.log(data)
            return conn.automoviles.clear().then(function() {
                console.log("Eliminado correctamente");
                data.forEach(function(item) {
                    console.log(item)
                    conn.automoviles.put({
                        'pk':item.pk,
                        'patente':item.fields.patente,
                        'modelo':item.fields.modelo,
                        'anio':item.fields.anio,
                        'estado':0
                    });      
                });
            });
        });
    }

    syncEliminar() {
        return this.conexion.automoviles.where('estado').equals('3').toArray()
        .then(function(data) {
            data.forEach(function(item){
                console.log(item);
                fetch('/api/eliminar-auto/'+item.id+'/')
                .then(function(e) {
                    new DAOAutomovil().eliminarRealmente(item.id);   
                });
            })
        });
    }

    syncAgregar() {
        conn = this.conexion;
        this.conexion.automoviles.where('estado').equals('4').toArray()
        .then(function(data) {
            data.forEach(function(item) {
                fetch('/api/agregar-auto/',{
                    method:'POST',
                    body: JSON.stringify({
                        patente:item.patente,
                        modelo:item.modelo,
                        marca_id:item.marca,
                        anio:item.anio,
                    }),
                    headers:{'Content-Type':'application/json'}
                }).then(function(respuesta){
                    return respuesta.json();
                }).then(function(data) {
                    console.log("sincronizado agregado correctamente");
                });
            });
        }).then(function() {
            //sincronizaremos toda la BBDD
            
            
        });
    }

}