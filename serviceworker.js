var CACHE_NAME = 'Mis Perris';
var urlsToCache = [
    '/',
    '/galeria/',
    '/formulario',
    '/agregar_mascota',
    '/listar_mascota',
    '/static/core/css/Estilos.css',
    '/static/core/css/agregar.css',
    '/static/core/css/formulario.css',
    '/static/core/css/listar.css',
    '/static/accounts/css/estilo_login.css',
    '/static/accounts/img/Duque.jpg',
    '/static/accounts/img/logo.jpg.png',
    '/static/core/img/logo_mascota.jpg',
    '/static/core/img/Apolo.jpg',
    '/static/core/img/Bigotes.jpg',
    '/static/core/img/Chocolate.jpg',
    '/static/core/img/crowfunding.jpg',
    '/static/core/img/Duque.jpg',
    '/static/core/img/kid-dog.jpg',
    '/static/core/img/logo.jpg.png',
    '/static/core/img/Luna.jpg',
    '/static/core/img/Maya.jpg',
    '/static/core/img/Oso.jpg',
    '/static/core/img/perro.png',
    '/static/core/img/Pexel.jpg',
    '/static/core/img/rescate.jpg',
    '/static/core/img/social-inst.png',
    '/static/core/img/social-twitter.png',
    '/static/core/img/socialfacebook.png',
    '/static/core/img/socialplus.png',
    '/static/core/img/Tom.jpg',
    '/static/core/img/Wifi.jpg',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.css',
    'https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.min.js',
    'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
    'https://code.jquery.com/jquery-3.3.1.slim.min.js',
    'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js',
    'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js',
    '/static/core/js/validar.js',
    '/static/core/js/Slider.js',
    '/static/core/js/agregar_validate.js',
    '/static/core/js/jquery.validate.min.js'
];

self.addEventListener('install', function(event) {
    // Perform install steps
    event.waitUntil(
      caches.open(CACHE_NAME)
        .then(function(cache) {
          console.log('Opened cache');
          return cache.addAll(urlsToCache);
        })
    );
});

self.addEventListener('fetch', function(event){
    event.respondWith(
        caches.match(event.request).then(function(response) {
            if(response) {
                return response;
            }

            return fetch(event.request);
        })
    );
});

importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var config = {
    apiKey: "AIzaSyDDlQmeCE3LXPj6L8y-sdt6L5PFrFXHsRQ",
    authDomain: "mis-perris-5c29c.firebaseapp.com",
    databaseURL: "https://mis-perris-5c29c.firebaseio.com",
    projectId: "mis-perris-5c29c",
    storageBucket: "mis-perris-5c29c.appspot.com",
    messagingSenderId: "546522154042"
};
firebase.initializeApp(config);

const messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function(payload){

    console.log(payload);
    var tituloNotficacion = "Mis Perris"
    var opciones = {
        body:'cuerpo del mensaje',
        icon:'/static/core/img/logo_mascota.jpg'
    }

});