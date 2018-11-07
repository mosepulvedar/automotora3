class Conexion {
    constructor() {
        this.nombreBD = "automotora_database";
        this.version = 2;
    }

    conectar() {
        var db  = new Dexie(this.nombreBD);
        db.version(this.version).stores({
            automoviles:'++id,pk,patente,modelo,anio,estado'
        });
        return db;
    }
}