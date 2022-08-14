document.addEventListener('DOMContentLoaded', function(){

    const products_box = document.querySelectorAll('.product_box');
        
        products_box.forEach(function(product){
            const bin = product.querySelector('#bin');
            console.log(bin);
            bin.addEventListener('click', () => delete_product_from_cart(product));
        })

})

function delete_product_from_cart(product){
    const product_info = product.querySelector('.product_info');
    const product_code = product_info.querySelector('.product_code').innerHTML;
    let size = (product_info.querySelector('.size').innerHTML);
    size = size.substr(6,)
    console.log(product_code)

    fetch('/cart', {
        method: 'DELETE',
        body: JSON.stringify({
            product_code: product_code,
            size : size,
        })
    })
    .then(response => response.json())
    .then(result =>
        console.log(result))
        product.innerHTML=''
}