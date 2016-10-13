(function() {

    angular
    .module('myApp')
    .controller('SetController', SetController);

    SetController.$inject = ['$scope','$http','$uibModal'];

    function SetController ($scope,$http) {
        $scope.classes =   classKey
        $scope.totalDisplayed = DISPLAY_LIMIT;
        $scope.tot = DISPLAY_LIMIT
        var oldId = 0    

        $scope.updateStream = {
            classe : 'Class'
        }


        $scope.loadMore = function () {
            if($scope.totalDisplayed + DISPLAY_LIMIT < $scope.tot)
                $scope.totalDisplayed += DISPLAY_LIMIT;  
            else if($scope.totalDisplayed != $scope.tot) 
                $scope.totalDisplayed = $scope.tot;

        };

        /*GET per avere tutti i channels*/
        $http.get("/channelsSet") 
            .success(function(data) { 
                $scope.channels = data
                $scope.tot = data.length
                if($scope.tot < DISPLAY_LIMIT)
                    $scope.totalDisplayed = $scope.tot;
                $(".loader").hide()
            }) 
            .error(function() { 
                showAlertBad("Si è verificato un errore!"); 
                $(".loader").hide()
            });



        /*Funzione che ritorna tutti i tag relativi ad un channel*/
        $scope.open = function (channelId,fieldId) {

            if(oldId != 0){
                var myEl = angular.element( document.querySelector( '#tr'+oldId ) );
                myEl[0].style.removeProperty('background-color')
            }

            var myEl = angular.element( document.querySelector( '#tr'+fieldId ) );
            myEl[0].style.setProperty('background-color','#80ff80','important')

            oldId = fieldId

            var url = "/getTags/" + channelId
            console.log(url)
            $http.get(url) 
                .success(function(data) { 
                    $scope.tags = data
                    var modalInstance = $uibModal.open({
                        templateUrl: 'myModalContent.html',
                        controller: 'ModalInstanceCtrl',
                        size: 'sm',
                        resolve: {
                            tags: function () {
                                return $scope.tags;
                            }
                        }
                    });
                }) 
                .error(function() { 
                    showAlertBad("Si è verificato un errore!"); 
                });
        }

        /*Funzione per aggiornare il set di un particolare field*/
        $scope.updateChannel = function(fieldId){
            oldId = 0
            var myEl = angular.element( document.querySelector( '#field'+fieldId ) );
            var set = ""
            if(myEl[0].value != "")
                set = myEl[0].value
            else
                set = myEl[0].placeholder

            set = set.trim()
            
            if(set != "Training" && set != "Test"){
                showAlertBad("Inserire una set valido")
                return;
            }
            var body = {field : fieldId, set: set}
            
            $http({
                method: 'POST',
                url: "/updateSet",
                data: $.param(body),
                headers: {'Content-Type': 'application/x-www-form-urlencoded'}
            })
            .success(function(data) { 
                    showAlert("Aggiornamento avvenuto con successo")
            }) 
            .error(function() { 
                showAlertBad("Si è verificato un errore!"); 
            }); 

        }



        /*Funzione che mostra gli stream della classe che viene selezionta dal dropdown menu*/
        $scope.showByType = function(set){
            oldId = 0
            $(".loader").show()
            var url = "/channelsBySet/" + set;
            $http.get(url) 
                .success(function(data) { 
                    $scope.channels = data
                    $scope.tot = data.length
                    if($scope.tot < DISPLAY_LIMIT)
                        $scope.totalDisplayed = $scope.tot;
                    showAlert("Success!");
                    $(".loader").hide() 
                }) 
                .error(function() { 
                showAlertBad("Si è verificato un errore!"); 
                   $(".loader").hide()
                });      
        }



        $scope.mostra = function(){
            oldId = 0
            $(".loader").show()
            if($scope.searchClass == undefined){
                showAlertBad("Scegliere una classe!")
                return;
            }

            var url = "/channelsSetByClass/" + $scope.searchClass;
            $http.get(url) 
                .success(function(data) { 
                    $scope.channels = data
                    $scope.tot = data.length
                    if($scope.tot < DISPLAY_LIMIT)
                        $scope.totalDisplayed = $scope.tot;
                    showAlert("Success!");
                    $(".loader").hide() 
                }) 
                .error(function() { 
                    showAlertBad("Si è verificato un errore!"); 
                    $(".loader").hide()
                });      
        }

    }

})();