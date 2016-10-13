(function() {

    angular
    .module('myApp')
    .controller('ClassificationController', ClassificationController);


    ClassificationController.$inject = ['$scope','$http','$uibModal'];

    function ClassificationController ($scope,$http,$uibModal) {
	    
		$scope.classes =  classKey
		$scope.totalDisplayed = DISPLAY_LIMIT;
		$scope.tot = DISPLAY_LIMIT
		var oldId = 0    
		$scope.numbers=[0,1,2,3,4,5,6,7,8,9]

		/*GET per avere tutti i channels*/
		$http.get("/getClassificationByNumber/0") 
			.success(function(data) { 
				$scope.fields = data
				$scope.tot = data.length
				if($scope.tot < DISPLAY_LIMIT)
					$scope.totalDisplayed = $scope.tot;
				$(".loader").hide()
			}) 
			.error(function() { 
				showAlertBad("Si è verificato un errore!"); 
				$(".loader").hide()
			});

		$scope.updateStream = {
			classe : 'Class'
		}


		$scope.loadMore = function () {
			if($scope.totalDisplayed + DISPLAY_LIMIT < $scope.tot)
				$scope.totalDisplayed += DISPLAY_LIMIT;  
			else if($scope.totalDisplayed != $scope.tot) 
				$scope.totalDisplayed = $scope.tot;
		};

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
		};


		$scope.showNUmber = function(){
			$(".loader").show()
			if($scope.searchNumber == undefined || $scope.searchType == undefined){
				showAlertBad("Scegliere un valore ed un tipo!")
				return;
			}

			var url = "/getClassificationByNumber/" + $scope.searchNumber;
				
			$http.get(url) 
				.success(function(data) { 
					$scope.fields = data
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

































