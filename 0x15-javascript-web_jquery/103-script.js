$(document).ready(function() {
  $('#btn_translate').click(fetchTranslation);
  $('#language_code').keypress(function(event) {
    if (event.key === 'Enter') {
      fetchTranslation();
    }
  });
  function fetchTranslation() {
    const languageCode = $('#language_code').val();
    const baseUrl = 'https://www.fourtonfish.com/hellosalut/hello/?lang=';
    const url = baseUrl + ${languageCode};
        
    $.get(url, function(data) {
      $('#hello').text(data.hello);
    });
  }
});

