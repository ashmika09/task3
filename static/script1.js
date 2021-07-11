var search=document.getElementById("search");
var imgArr=document.getElementsByClassName("movieimg");
var infoArr=document.getElementsByClassName("info");

search.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
    console.log("pressed enter");
    getQuery(search.value)
        .then(function(results){
            console.log("results :",results);
            var filteredResults=results.filter(result=>result.backdrop_path);
            for(let i=0; i<8;i++){
                imgArr[i].src="https://image.tmdb.org/t/p/w500"+filteredResults[i].backdrop_path;
                infoArr[i].innerHTML=`<strong>${filteredResults[i].original_title}</strong><br><br>
                                      IMDB Rating  : ${filteredResults[i].vote_average}<br>
                                      Release-date : ${filteredResults[i].release_date}`;
            }
        })
        .catch(err=>console.error(err));
  }
}); 

const getQuery=async function(query){ 
    const response=await fetch(`https://api.themoviedb.org/3/search/movie?api_key=f8c61ba8b87e28b16fd664a36b974f41&query=${query}`);
    const data=await response.json();
    if(response.status!==200){
        throw new Error("Error!");
    }
    return data.results;
}

const getQueryDetails=async function(query){ 
    const response=await fetch(`https://api.themoviedb.org/3/movie/${ID}?api_key=f8c61ba8b87e28b16fd664a36b974f41&query=${query}`);
    const data=await response.json();
    if(response.status!==200){
        throw new Error("Error! ");                  
    }
    return data.results;
}