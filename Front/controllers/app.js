// Encerrar nuestro javascript en paréntesis es buen hábito.
(function() {
    var app = angular.module('ModuloResidentes', []); // Declaramos un modulo y el nombre de la aplicación "tienda"

    app.controller('Residentes', function(){ // Declaramos el controlador llamado "tiendaCodejobs"
        this.inforesidente = residente; // Establecer una propiedad (product) igual al objeto.
    });

    var residente = [{
        name: 'Ivan Serre',
        dpto: 11,
        description: 'encontro una de las palabras mas oscuras de la lengua del latin',
        puedeFirmar:true,
        Nohabitado:false,
        reclamos:[{
          fecha:"2017-10-10",
          description: "es simplemente el texto de relleno de las imprentas y archivos de texto"
         },{
          fecha:"2017-01-01",
          description: "Es un hecho establecido hace demasiado tiempo que un lector se distraera con el contenido del texto de un sitio mientras que mira su diseno"
         }]
    },{
        name: 'Juanito Perez',
        dpto: 120,
        description: 'Al contrario del pensamiento popular, el texto de Lorem Ipsum no es simplemente texto aleatorio.',
        puedeFirmar:true,
        Nohabitado:false,
        reclamos:[{
          fecha:"2017-10-10",
          description: "Hay muchas variaciones de los pasajes de Lorem Ipsum disponibles"
         },{
          fecha:"2017-01-01",
          description: "por Cicero, escrito en el año 45 antes de Cristo. Este libro es un tratado de teoria de eticas"
         }]
    }];
})();
