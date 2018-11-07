class DAOAutomovil {

    constructor() {
        this.conexion = new Conexion().conectar();
    }

    listarAutos() {
        return this
        .conexion
        .automoviles
        .where('estado')
        .notEqual('3')
        .toArray();
    }

    agregarAuto(pk=null,marca, modelo, anio, patente,estado) {
       return this.conexion.automoviles.put({
            pk:pk,
            patente:patente,
            modelo:modelo,
            marca:marca,
            anio:anio,
            estado: estado   
        })
    }

    eliminarAuto(id) {
        return this.conexion.automoviles.update(id, {'estado':'3'})
    }

    eliminarRealmente(id) {
        return this.conexion.automoviles.delete(id);
    }

    modificarEstado(id, estado) {
        return this.conexion.automoviles.update(id, {'estado:':estao});
    }

} 