$(document).ready(function(){
    $('.increment-btn').click(function (e){
        e.preventDefault();
        var inc_value = $(this).closest('.product-data').find('.qty-input').val();
        var value=parseInt(inc_value,10);
        value=isNaN(value) ? 0 : value;
        
        if(value<10){
            value++;
            $(this).closest('.product-data').find('.qty-input').val(value);
        }
    });

    $('.decrement-btn').click(function (e){
        e.preventDefault();
        var dec_value = $(this).closest('.product-data').find('.qty-input').val();
        var value=parseInt(dec_value,10);
        value=isNaN(value) ? 0 : value;
        
        if(value>1){
            value--;
            $(this).closest('.product-data').find('.qty-input').val(value);
        }
    });


    $('.addToCartBtn').click(function (e){
        e.preventDefault();
        var product_id = $(this).closest('.product-data').find('.prod-id').val();
        var product_qty = $(this).closest('.product-data').find('.qty-input').val();
        var token= $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/addtocart",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                csrfmiddlewaretoken: token
            },
            success: function(response){
                console.log(response);
                alertify.success(response.status);
            }

        });
    });


    $('.changeQuantity').click(function (e){
        e.preventDefault();
        var product_id = $(this).closest('.product-data').find('.prod-id').val();
        var product_qty = $(this).closest('.product-data').find('.qty-input').val();
        var token= $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/updatecart",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                csrfmiddlewaretoken: token
            },
            success: function(response){
                console.log(response);
                // alertify.success(response.status);
            }

        });
    });

    $('.delete-cart-item').click(function (e){
        e.preventDefault();
        var product_id = $(this).closest('.product-data').find('.prod-id').val();
        var token= $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/deletecartitem",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
            success: function(response){
                console.log(response);
                alertify.success(response.status);

                // 
                $('.cartdata').load(location.href + " .cartdata");
            }

        });
    });


    $('.addToWishlist').click(function (e){
        e.preventDefault();
        var product_id = $(this).closest('.product-data').find('.prod-id').val();
        var token= $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/addtowishlist",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
            success: function(response){
                console.log(response);
                alertify.success(response.status);
            }

        });
    });


    $('.delete-wishlist-item').click(function (e){
        e.preventDefault();
        var product_id = $(this).closest('.product-data').find('.prod-id').val();
        var token= $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/deletewishlistitem",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
            success: function(response){
                console.log(response);
                alertify.success(response.status);

                // 
                $('.cartdata').load(location.href + " .cartdata");
            }

        });
    });

});

