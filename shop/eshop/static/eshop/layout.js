document.addEventListener('DOMContentLoaded', function() {
    
    if(document.querySelector('#logout')){
        get_count_of_cart()
    }

    
})


function get_count_of_cart() {
    fetch('/get_count_of_cart')
    .then(response => response.json())
    .then(result => {
        console.log(result)
        document.querySelector('#cart_value').innerHTML = result.count_of_cart;
    })

}

