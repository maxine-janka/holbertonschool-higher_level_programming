
document.addEventListener('DOMContentLoaded', getMovieTitles) //HTML doc fully parsed before calling

async function getMovieTitles() {
  movieList = document.getElementById('list_movies');
  const url = "https://swapi-api.hbtn.io/api/films/?format=json";

    try {
      const response = await fetch(url); //Send GET request
      if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
      }
      const jsonData = await response.json(); //Await response and store data
  
      const movies = jsonData.results; //Store movie arrays

      //Iterate each array and extract title
      movies.forEach(movie => {
        // console.log(movie.title);
        const movieTitle = document.createElement('li');
        movieTitle.textContent = movie.title;
        movieList.append(movieTitle);
      });
      } catch (error) {
        console.error(error.message);
    }
  } 
 
