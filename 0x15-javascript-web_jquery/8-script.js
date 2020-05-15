$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (body) {
  const elements = body.results;
  for (const x in elements) {
    $('<li>' + elements[x].title + '</li>').appendTo('UL#list_movies');
  }
});
