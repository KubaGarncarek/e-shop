
document.addEventListener('DOMContentLoaded', function() {

    // let available_sizes = JSON.parse(document.getElementById('available_sizes').textContent)
    // console.log(product);
    // console.log(available_sizes);
    var choosen_size;
    let str_product_code = document.querySelector('#product_code').innerHTML;
    var product_code = str_product_code.substr(7,);
    
    const sizes_area = document.querySelector(".sizes");
    const sizes_box = sizes_area.querySelectorAll('button');
    sizes_box.forEach(function(size) {

        size.onclick = function() {
            choosen_size = size.innerHTML;
            console.log(choosen_size);
        }
    })



    const cart = document.querySelector('#cart');
    cart.addEventListener('click', () => {
        if (document.querySelector('#login')){
            force_login();
        } else {
            add_product_to_cart(choosen_size,product_code);
            
        }
    })
    const favorites = document.querySelector('#favorites');

});




function add_product_to_cart(choosen_size, product_code) {
    
    const cart_value = document.getElementById('cart_value');
    let count_of_cart = cart_value.innerHTML;
    console.log(count_of_cart);
    count_of_cart++; 
    console.log(count_of_cart);
    cart_value.innerHTML = count_of_cart;

    fetch('/cart',{
        method: 'POST',
        body: JSON.stringify({
            product_code : product_code,
            size : choosen_size.substr(3,),
        })
    })
    .then(response => response.json)
    .then(result => {
        console.log(result);
    })

    
}


function force_login() {
    window.location.href = "http://127.0.0.1:8000/login";
}

