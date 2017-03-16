var LabsApp = angular.module('app', []);

LabsApp.controller('GroupCtrl', function($scope, $http){

  $scope.choiseSubject = function(subjId) {
    $http.get('/api/subject/'+subjId).then(successCb, errorCb);
    function successCb(response){
      $scope.subject = response.data;
      menuClose();
    };
    function errorCb(response) {
      console.log('error ' + response.status);
    };
  };
});



LabsApp.controller('ShedulGroupCtrl', function($scope, $http){

  $http.get('/api/currentweek/').then(function success(response){
    $scope.curWeek = response.data.curWeek + ' учебная неделя';
  },function error(response){
    console.log('error ' + response.status);
  });

  $scope.choiseAction = 1;
  $scope.qGroup = '';

  $scope.changeChoiseAction = function(id){
    $scope.choiseAction = id;
  };



  function successCb(response){
    $scope.groups = response.data;
    $scope.qGroup = 'группа с номером ' + $scope.requestGroup + ' не найдена';
  };

  function errorCb(response) {
    console.log('error ' + response.status);
  };

  $scope.submit = function () {
    switch ($scope.choiseAction) {
      case 2:
            $http({
              url: '/api/shedul/',
              method: 'GET',
              params: {
                group_name: $scope.requestGroup
              }
            }).then(successCb, errorCb);
            break;
      case 1:
            break;
    }

  };
});


LabsApp.directive("aver", function () {
  return {
    link: function(scope, element, attrs){
      element.css('height', '700px');
    }
  };
});
