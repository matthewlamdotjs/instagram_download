function scrape(url) {
  let imageUrl = "";
  /*$.get(url, function(response) {
    imageUrl = response.toString().split("<meta property=\"og:image\" content=")[1].split("\"")[1];
  });*/
  $.ajax({
    async: false,
    type: 'GET',
    url: url,
    success: function(response) {
      imageUrl = response.toString().split("<meta property=\"og:image\" content=")[1].split("\"")[1];
    }
  });
  //let fileName = imgUrl.split("/")[-1];
  return imageUrl; // returns undefined
}

//TEST
//scrape("https://www.instagram.com/p/BfKjQxcgv-E/");
