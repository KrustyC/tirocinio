(function () {

    function route($routeProvider){
        $routeProvider.
            when('/', {
                templateUrl: '/static/partials/index/index.html',
                controller: 'MainController'
            }).
            when('/info', {
                templateUrl: '../static/partials/info/info.html',
                controller: 'InfoController'
            }).
            when('/set', {
                templateUrl: '../static/partials/set/set.html',
                controller: 'SetController'
            }).
            when('/classification', {
                templateUrl: '../static/partials/classification/classification.html',
                controller: 'ClassificationController'
            }).
            when('/classificationRelevant', {
                templateUrl: '../static/partials/classificationRelevant/classificationRelevant.html',
                controller: 'ClassificationRelevantController'
            }).
            when('/metrics', {
                templateUrl: '../static/partials/metrics/metrics.html',
                controller: 'MetricsController'
            }).
            when('/metricsRelevant', {
                templateUrl: '../static/partials/metricsRelevant/metricsRelevant.html',
                controller: 'MetricsRelevantController'
            }).
            when('/matrix', {
                templateUrl: '../static/partials/matrix/matrix.html',
                controller: 'MatrixController'
            }).
            when('/matrixRelevant', {
                templateUrl: '../static/partials/matrixRelevant/matrixRelevant.html',
                controller: 'MatrixRelevantController'
            }).
            otherwise({
                redirectTo: '/'
            });
    }

    /*Sostiuisco le {{ }} di angular con le [[ ]] a causa di un problema di parsing con Flask*/
    function config($interpolateProvider){
        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');
    }

    angular
        .module('myApp')
        .config(['$routeProvider', route])
        .config(['$interpolateProvider', config]);
})();