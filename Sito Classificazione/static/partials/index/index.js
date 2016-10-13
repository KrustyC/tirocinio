(function() {

	angular
	.module('myApp')
	.controller('MainController', MainController);


	MainController.$inject = ['$scope','$http','$uibModal'];

    function MainController ($scope,$http,$uibModal) {
		$scope.classes =   classKey
		$scope.totalDisplayed = DISPLAY_LIMIT;
		$scope.tot = DISPLAY_LIMIT
		var oldId = 0    

		$scope.updateStream = {
			classe : 'Class'
		}

		/*GET per avere tutti i channels*/
		$http.get("/channels") 
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
		}

		/*Funzione per eliminare un particolare stream*/
		$scope.deleteChannel = function(fieldId){
			oldId = 0
			var url = "/deleteField/" + fieldId
			$http.delete(url) 
				.success(function(data) { 
					showAlert("Eliminazione avvenuta con successo")
					$scope.tot -= 1
					$scope.totalDisplayed -= 1
					for(c in $scope.channels){
						if($scope.channels[c].field_id === fieldId )
							$scope.channels.splice(c,1)
					}
				}) 
				.error(function() { 
					showAlertBad("Si è verificato un errore!"); 
				}); 
		}


		 /*Funzione per aggiornare la calsse di un particolare stream ritenuto inopportuno*/
		$scope.updateChannel = function(fieldId){
			oldId = 0
			var myEl = angular.element( document.querySelector( '#field'+fieldId ) );
			var classe = ""
			if(myEl[0].value != "")
				classe = myEl[0].value
			else
				classe = myEl[0].placeholder

			if(classKey.indexOf(classe) < 0){
				showAlertBad("Inserire una classe valida")
				return;
			}
			var body = {field : fieldId, classe: classe}

			$http({
				method: 'POST',
				url: "/updateClass",
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

    	/*GET per avere tutti i channels---Utilizzata sia per averli tutti che per avere solo quelli non classifficate*/
		$scope.refresh = function(url){
			oldId = 0
			$(".loader").show()
			$http.get(url) 
				.success(function(data) { 
					showAlert("Refresh ok!"); 
					$scope.totalDisplayed = DISPLAY_LIMIT;
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
		}

		/*Funzione che mostra gli stream della classe che viene selezionta dal dropdown menu*/
		$scope.mostra = function(){
			oldId = 0
			$(".loader").show()
			if($scope.searchClass == undefined){
				showAlertBad("Scegliere una classe!")
				return;
			}

			var url = "/getClassStream/" + $scope.searchClass;
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


