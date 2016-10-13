(function() {

    angular
    .module('myApp')
    .controller('InfoController', InfoController);


    InfoController.$inject = ['$scope','$http'];

    function InfoController ($scope,$http) {
    
        $scope.classPercentage = 0
        $scope.classes =  classKey
        $http.get("/getInfo") 
            .success(function(data) { 
                $scope.info = data;
                $(".loader").hide()
            }) 
            .error(function() { 
                showAlertBad("Si è verificato un errore!"); 
                $(".loader").hide()
            });      

        $scope.classCount = function(){
            $(".loader").show()
            if($scope.myClass == undefined){
                showAlertBad("Scegliere una classe!")
                return;
            }

            var url = "/classCount/" + $scope.myClass;
            $http.get(url) 
                .success(function(data) { 
                    $scope.streamClasse = data.streamClasse
                    var percentage = data.streamClasse/$scope.info.totCount * 100
                    $scope.classPercentage = percentage.toFixed(2)
                    $(".loader").hide()
                }) 
                .error(function() { 
                    showAlertBad("Si è verificato un errore!"); 
                    $(".loader").hide()
                });      
        }   
    }
})();
