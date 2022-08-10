
document.addEventListener('DOMContentLoaded', function() {
    let product = JSON.parse(document.getElementById('product').textContent)
    let available_sizes = JSON.parse(document.getElementById('available_sizes').textContent)

    console.log(product);
    console.log(available_sizes);

    const cart = document.querySelector('#cart');
    const favorites = document.querySelector('#favorites');

   
    cart.addEventListener('click', () => {
        if (document.querySelector('#login')){
            force_login();
        }
    })

});


function force_login() {
    window.location.href = "http://127.0.0.1:8000/login";
}