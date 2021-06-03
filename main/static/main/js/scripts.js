var cart = {};

$(document).ready(function () {
    CheckCart()
    AddToCart()
    ShowCart()
});

function AddToCart(){
    var form = $('#BuyForm');
    console.log(form);
    form.on('submit', function(e) {
        e.preventDefault();
        var buy_btn = $('#buy-btn');
        var post_name = buy_btn.data("name");
        var post_id = buy_btn.data("id");
        var post_category = buy_btn.data("categoty");
        var post_slug = String(buy_btn.data("slug"));
        var post_price = $('input[name=oplata]:checked').val();
           
        console.log(post_category);
        console.log(post_id);
        console.log(post_name);
        console.log(post_price);
        console.log(post_slug);
        
        if (cart[post_id] != undefined) {
            cart[post_id][2] ++
        }
        else {
            cart[post_id] = [post_name, post_price, 1, post_slug]
        }
        
        localStorage.setItem('cart', JSON.stringify(cart) )
        CheckCart()
        ShowCart()
    }) 
}

function CheckCart() {
    if (localStorage.getItem('cart') != null) {
        cart = JSON.parse(localStorage.getItem('cart'))
        console.log(cart)
    }
}

function ShowCart(){
    if ($.isEmptyObject(cart)){
        var out = '<li><a class="dropdown-item lead disabled" href="#">Корзина пуста</a></li>'
        $('.basket-items').html(out)
        price = 0
    }
    else {
        var out = ''
        for (var i in cart){
            //out += '<li><a class="dropdown-item lead" href="'+'http://127.0.0.1:8000/post/'+cart[i][3]+'">' + cart[i][0] + ' --- ' + cart[i][1] +'₽</a></li>';
            //out += '<li><a class="dropdown-item" href="'+'http://127.0.0.1:8000/post/'+cart[i][3]+'"><div class="card card-how-low" style="width:300px"><div class="card-body"><div class="row"><div class="col-7"><h5 class="card-title">' + cart[i][0] + '</h5><h6 class="card-subtitle mb-2 text-muted ">' + cart[i][1] +'</h6></div><div class="col-5"><h5>123123</h5></div></div></div></div></a></li>';
            out +='<li>\
                        <div class="card card-how-low mx-1 mx-sm-2 my-2" style="width:325px">\
                            <div class="card-body"><div class="row">\
                                <div class="col-6">\
                                    <h5 class="card-title">' + cart[i][0] + '</h5>\
                                    <h6 class="card-subtitle mb-2 text-muted ">' + cart[i][1] +' ₽ x '+cart[i][2]+' шт. </h6>\
                                </div>\
                                <div class="col-6 text-center">\
                                    <div class="btn-group rounded" role="group" aria-label="Basic example">\
                                        <button type="button" data-art="'+ i +'" class="minus btn pb-2 btn-light">\
                                            <i class="bi bi-dash" style="font-size: 20px;"></i>\
                                        </button>\
                                        <button type="button" data-art="'+ i +'" class="plus btn pb-2 btn-light">\
                                            <i class="bi bi-plus" style="font-size: 22px;"></i>\
                                        </button>\
                                        <button type="button" class="btn pb-2 btn-light">\
                                            <a href="http://127.0.0.1:8000/post/'+cart[i][3]+'"\
                                            <i class="bi bi-arrows-fullscreen" style="font-size: 20px;"></i>\
                                            </a>\
                                        </button>\
                                    </div>\
                                </div>\
                            </div>\
                        </div>\
                    </li>';
            
        }

        price = 0
        for (var i in cart)
            price += Number(cart[i][1]) * cart[i][2]

        out += '<li><hr class="dropdown-divider mt-2"></li>\
                <li>\
                    <div class="row mx-1">\
                    <div class="col-7">\
                        <h5 class="lead mt-2 text-muted" style="font-size:18px"><b>Стоимость: '+price+' ₽</b></h5>\
                    </div>\
                    <div class="col-5 text-right">\
                        <a href="http://127.0.0.1:8000/order" class="btn btn-primary">\
                        Покупка\
                        </a>\
                    </div>\
                    </div>\
                </li>';
    }
    
    OrderCart()
    $('.basket-items').html(out)
    $('.plus').on('click',PlusDoor)
    $('.minus').on('click',MinusDoor)
}

function PlusDoor(){
    var articul = $(this).attr('data-art')
    cart[articul][2]++
    localStorage.setItem('cart', JSON.stringify(cart))
    ShowCart()   
}

function MinusDoor(){
    var articul = $(this).attr('data-art')
    if (cart[articul][2]>1){
        cart[articul][2]--
    }
    else {
        delete cart[articul]
    
    }
    localStorage.setItem('cart', JSON.stringify(cart)) 
    ShowCart()
}

function TotalPrice(){
    price = 0
    for (var i in cart)
        price += Number(cart[i][1]) * cart[i][2]
}

function OrderCart(){
    var OrderOut = ''
    if ($.isEmptyObject(cart)){
        $('#CartList').val('')
        $('#btn-order').addClass('disabled');
        $('.Total-pr').text('Похоже вы удалили все товары из корзины, но не беда, вы всегда найдёте у нас то, что вам по вкусу');
    }
    else {
        for (var i in cart)
            OrderOut += 'Товар: ' + cart[i][0] +';   Артикул: '+cart[i][3]+ ';   Цена: '+ cart[i][1] +' ₽;   Кол-во: '+cart[i][2]+ ' шт;   Ссылка: http://127.0.0.1:8000/post/'+cart[i][3]+'\n'
            $('#CartList').val(OrderOut)

        $('#CartList').val($('#CartList').val() + '\n'+'Общая стоимость: '+price+' ₽');
        $('#btn-order').removeClass('disabled');
        $('.Total-pr').text('Общая сумма заказа составляет: '+price+' рублей');
    }
}