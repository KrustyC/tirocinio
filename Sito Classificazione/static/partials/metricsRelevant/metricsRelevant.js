(function() {

    angular
    .module('myApp')
    .controller('MetricsRelevantController', MetricsRelevantController);


    MetricsRelevantController.$inject = ['$scope','$http','$uibModal'];

    function MetricsRelevantController ($scope,$http,$uibModal) {

        $scope.classes =   classKey
        $scope.totalDisplayed = DISPLAY_LIMIT;
        $scope.tot = DISPLAY_LIMIT
        $scope.numbers=[0,1,2,3,4,5,6,7,8,9]
        var oldId = 0    


        $scope.updateStream = {
            classe : 'Class'
        }

        /*GET per avere tutti i channels*/
        $http.get("/getMetricsRelevantByNumber/0") 
            .success(function(data) { 
                $scope.metrics = data
                $scope.tot = data.length
                if($scope.tot < DISPLAY_LIMIT)
                    $scope.totalDisplayed = $scope.tot;
                $(".loader").hide()
            }) 
            .error(function() { 
                showAlertBad("Si è verificato un errore!"); 
                $(".loader").hide()
            });

        $scope.loadMore = function () {
            if($scope.totalDisplayed + DISPLAY_LIMIT < $scope.tot)
                $scope.totalDisplayed += DISPLAY_LIMIT;  
            else if($scope.totalDisplayed != $scope.tot) 
                $scope.totalDisplayed = $scope.tot;
        };

        $scope.getTotalMetrics = function () {
            $http.get("/getTotalRelevantMetrics") 
                .success(function(data) { 
                    $scope.metrics = data
                    $scope.tot = data.length
                    if($scope.tot < DISPLAY_LIMIT)
                        $scope.totalDisplayed = $scope.tot;
                    $(".loader").hide()
                    showAlert("Caricato!"); 
                }) 
                .error(function() { 
                    showAlertBad("Si è verificato un errore!"); 
                    $(".loader").hide()
                });
        };

           

        $scope.showNUmber = function(){
            $(".loader").show()
            if($scope.searchNumber == undefined){
                showAlertBad("Scegliere un valore!")
                return;
            }

            var url = "/getMetricsRelevantByNumber/" + $scope.searchNumber;
            $http.get(url) 
                .success(function(data) { 
                    $scope.metrics = data
                    showAlert("Caricato!")
                    $(".loader").hide()
                }) 
                .error(function() { 
                    showAlertBad("Si è verificato un errore!"); 
                    $(".loader").hide()
                });      
        }
    
    }

})();












