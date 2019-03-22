var app = angular.module('app', ['ngMaterial', 'ngMessages']);

app.config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{[{');
	$interpolateProvider.endSymbol('}]}');
});

app.controller('ctrl', ['$scope', '$http', function ($scope, $http) {
	$scope.search = {
		"count": 1
	};
	$scope.tweets = [];
	$scope.get_tweets = function () {
		$http.post('/sentiment', $scope.search).then(function (data) {
			$scope.tweets = data.data;
		}, function () {
			console.log("error")
		});
	}
}]);

