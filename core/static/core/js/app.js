

function eliminar(id) {
    
    new DAOAutomovil()
    .eliminarAuto(id)
    .then(function(e){
        new SyncAuto().syncEliminar();
        dibujarTabla()
    });
}

function dibujarTabla() {

    dAuto = new DAOAutomovil();
    
    dAuto
    .listarAutos()
    .then(function(d) {
      
        var html=`<tr>
        <th>Patente</th>
        <th>Marca</th>
        <th>Modelo</th>
        <th>Año</th>
        <th>Opciones</th>
    </tr>`;
        d.forEach(function(data) {
            
            html+="<tr>";
            html+= "<tr>";
            html+="<td>";
            html+=data.patente;
            html+="</td>";
            html+="<td>";
            html+=data.modelo;
            html+="</td>";
            html+="<td>";
            html+=data.anio;
            html+="</td>";
            html+="<td>";
            html+="pendiente";
            html+="</td>";
            html+="<td>";
            html+="<button onclick='eliminar("+data.id+")'>Eliminar</button>";
            html+="</td>";
            html+="</tr>";
        });
        var tabla = document.getElementById("tablaAutos")
        tabla.innerHTML = html
    });
}

window.addEventListener('load', function() {

   new SyncAuto()
   .SyncAutos()
   .then(function() {
       dibujarTabla();
   })
   .catch(function(){
       console.log("fallo")
       dibujarTabla();
   });

   function updateOnlineStatus(event) {
    var estado = document.getElementById("estado_web");
       
    if (navigator.onLine) {
      // handle online status
      estado.style="display:none";
      console.log('online');
      a  = new SyncAuto();
      a.syncEliminar().then(function() {
          return a.syncAgregar();
      });
    } else {
      // handle offline status
      estado.style = "display:block";
      console.log('offline');
    }
  }

  window.addEventListener('online', updateOnlineStatus);
  window.addEventListener('offline', updateOnlineStatus);
});

function guardarAuto() {
    aDAO = new DAOAutomovil();
    aDAO.agregarAuto(
        null,
        document.getElementById("cboMarca").value,
        document.getElementById("txtModelo").value,
        document.getElementById("txtAnio").value,
        document.getElementById("txtPatente").value,
        '4'
    ).then(function() {
        console.log("agregado correctamente")
        new SyncAuto().syncAgregar();
    });
}