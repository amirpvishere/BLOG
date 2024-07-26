function like(slug, pk) {
    var element = document.getElementById("like")
    var count = document.getElementById("count")
    $.get(`/post/like/${slug}/${pk}`).then(response =>{
        if(response['response'] === "like") {
            element.className = "fa fa-heart"
            count.innerText = Number(count.innerText) + 1
        }else{
            element.className = "fa fa-heart-o"
            count.innerText = Number(count.innerText) - 1
        }
    });
}