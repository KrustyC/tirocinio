(function() {

    angular
    .module('myApp')
    .controller('ModalInstanceCtrl', ModalInstanceCtrl);


    ModalInstanceCtrl.$inject = ['$scope','$uibModalInstance', 'tags'];

	function ModalInstanceCtrl ($scope, $uibModalInstance, tags) {
		$scope.tags = tags;

		$scope.cancel = function () {
			$uibModalInstance.dismiss('cancel');
		};	
	}   


})();