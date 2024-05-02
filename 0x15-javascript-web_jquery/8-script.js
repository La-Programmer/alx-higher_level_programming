$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (data) {
      $.each(data.results, function (index, item) {
        $('#list_movies').append('<li>' + item.title + '</li>');
      });
    }
  });
});
