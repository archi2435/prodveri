 $(document).ready(function () {
    var form = $('#BuyForm');
    console.log(form);
    form.on('submit', function(e) {
        e.preventDefault();
        var buy_btn = $('#buy-btn');
        var post_name = buy_btn.data("name");
        var post_id = buy_btn.data("id");
        var post_category = buy_btn.data("categoty");
        var post_price = $('input[name=oplata]:checked').val();
        
        
        console.log(post_category);
        console.log(post_id);
        console.log(post_name);
        console.log(post_price);
        
        $('.basket-items').append('<li><a class="dropdown-item" href="#">' + post_name +' '+ post_price +'₽</a></li>');
    })
    
 });