function AppController ($scope, $http) {
  $scope.message = "Am I working?";
  $http.get("api/pin").success(function (data) {
    $scope.pins = data.objects;
  });

  $scope.addPin = function () {
    $http.post("api/pin", {"title":"new", "image":"http://placekitten.com/200/200/?image="
      + $scope.pins.length})
      .success(function (data) {
        $scope.pins.push(data);
      })
  }

  $scope.deletePin = function (pin) {
    $http.delete("api/pin/" + pin.id).success(function(response) {
      $scope.pins.splice($scope.pins.indexOf(pin), 1);
    })
  }

  $scope.updatePin = function (pin) {
    $http.put("api/pin/" + pin.id, pin);
  }
}

