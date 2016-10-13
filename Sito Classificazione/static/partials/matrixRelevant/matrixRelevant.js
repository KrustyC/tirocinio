(function() {

    angular
    .module('myApp')
    .controller('MatrixRelevantController', MatrixRelevantController);


    MatrixRelevantController.$inject = ['$scope','$http','$uibModal'];

    function MatrixRelevantController ($scope,$http,$uibModal) {

        $scope.numbers=[0,1,2,3,4,5,6,7,8,9]

        $http.get("/getConfusionMatrix/0") 
            .success(function(data) { 
                $scope.rows = data
                $(".loader").hide()
            }) 
            .error(function() { 
                showAlertBad("Si è verificato un errore!"); 
                $(".loader").hide()
            });

        $scope.showNUmber = function(){
        
            $(".loader").show()
            if($scope.searchNumber == undefined){
                showAlertBad("Scegliere un valore!")
                return;
            }

            var url = "/getConfusionMatrix/" + $scope.searchNumber;
            $http.get(url) 
                .success(function(data) { 
                    $scope.rows = data
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