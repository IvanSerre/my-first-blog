// Encerrar nuestro javascript en paréntesis es buen hábito.
(function() {
    var app = angular.module('ModuloResidentes', []); // Declaramos un modulo y el nombre de la aplicación "tienda"

    app.controller('Residentes', function($scope, $http){
     debugger;
     $http.get("http://127.0.0.1:8000/ListResidentes/?format=json").then(function(response){
      debugger;
       this.inforesidente = response.data;
     });
    });
})();
