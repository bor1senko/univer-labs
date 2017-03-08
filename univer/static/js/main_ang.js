var LabsApp = angular.module('app', []);

LabsApp.controller('GroupCtrl', function($scope, $http){

  $scope.choiseSubject = function(subjId) {
    $http.get('/api/subject/'+subjId).then(successCb, errorCb);
    function successCb(response){
      $scope.subject = response.data;
    };
    function errorCb(response) {
      console.log('error ' + response.status);
    };
  };
});
