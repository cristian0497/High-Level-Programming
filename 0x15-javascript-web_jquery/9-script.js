$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (body) {
  $('#hello').text(body.hello);
});
