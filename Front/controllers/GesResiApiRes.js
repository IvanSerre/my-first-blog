// Encerrar nuestro javascript en paréntesis es buen hábito.
(
function()
{
    var app = angular.module('ModuloResidentes', []); // Declaramos un modulo y el nombre de la aplicación "tienda"
    app.controller('Residentes', function($scope, $http){

     Objresidentes  = this;
     $http({
           method:'get',
           url: 'http://ivanserre.pythonanywhere.com/ListResidentes/',
           params: {
            format: 'json',
            callback: 'JSON_CALLBACK'
           }
         }).then(function(res){
           Objresidentes.inforesidente = res.data;
         }, function(error){
            alert(error.data);
         });
    });
})();
