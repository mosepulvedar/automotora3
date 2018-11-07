//This is the "Offline page" service worker

//Install stage sets up the offline page in the cache and opens a new cache
self.addEventListener('install', function(event) {
    var offlinePage = new Request('/');
    event.waitUntil(
      caches.open("pwabuilder-offline")
      .then(function(cache) {
        return cache.addAll([
          '/static/core/css/estilos.css',
          '/',
          '/static/core/img/automovillogo.jpg',
          'https://unpkg.com/dexie@latest/dist/dexie.js',
          '/listar-autos/',
          '/static/core/js/conexion.js',
          '/static/core/js/app.js',
          '/static/core/js/SyncAuto.js',
          '/static/core/js/DAOAutomovil.js',
          '/static/core/img/automovil.png',
          '/static/core/img/social-twitter.png',
          'https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js',
          'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.css',
          'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.min.js',
          '/static/core/img/escarabajo.png',
          '/agregar-auto/'
        ])
    }));
  });
  
  //If any fetch fails, it will show the offline page.
  //Maybe this should be limited to HTML documents?
  self.addEventListener('fetch', function(event) {
    event.respondWith(
      fetch(event.request).catch(function(error) {
        console.error( '[PWA Builder] Network request Failed. Serving offline page ' + error );
        return caches.open('pwabuilder-offline').then(function(cache) {
          console.log(event.request);
          return cache.match(event.request);
        });
      }
    ));
  });
  
  //This is a event that can be fired from your page to tell the SW to update the offline page
  self.addEventListener('refreshOffline', function(response) {
    return caches.open('pwabuilder-offline').then(function(cache) {
      console.log('[PWA Builder] Offline page updated from refreshOffline event: '+ response.url);
      return cache.put(offlinePage, response);
    });
  });
  