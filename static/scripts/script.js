var app = angular.module('app', ['ngMaterial', 'ngMessages']);

app.config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{[{');
	$interpolateProvider.endSymbol('}]}');
});

const RIGHT_KEY = 39;
const SPACE_KEY = 32;
const LEFT_KEY = 37;
const BACKSPACE_KEY = 8;


app.controller('ctrl', ['$scope', '$http', function ($scope, $http) {
	$scope.search = {
		"count": 1
	};
	$scope.tweets = [];
	$scope.get_tweets = function () {
		$http.post('/sentiment', $scope.search).then(function (data) {
			console.log(data);
			$scope.tweets = data.data;
		}, function () {
			console.log("error")
		});
	}
}]);

