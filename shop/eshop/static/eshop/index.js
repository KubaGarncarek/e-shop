

document.addEventListener('DOMContentLoaded',function() {
    load_products();
})


function load_products() {
    fetch('load_products')
    .then(response => response.json())
    .then(result => {
        console.log(result.products);
        result.products.forEach(product => create_product_box(product))

    })
}

function create_product_box(product) {

    const main = document.querySelector('#main');
    const product_box = document.createElement('div');
    const photo = document.createElement('img');
    photo.src = product.photo;
    const name = document.createElement('div');
    name.innerHTML = product.name;
    console.log(product.name)

    product_box.append(photo);
    product_box.appendChild(name);
    
    main.appendChild(product_box);
    console.log(product.id);

    product_box.addEventListener('click', () => load_product_page(product.id));

}

function load_product_page(product_id) {

    window.location.href = `http://127.0.0.1:8000/load_product_page/${product_id}`;
    
}

