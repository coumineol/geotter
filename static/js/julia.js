
$( document ).ready(function() {

    $('#get-followers').on('click', function() {

        $('html,body').css('cursor','progress');

        $.ajaxSetup({
                beforeSend: function(xhr, settings) {
                    csrftoken = getCookie('csrftoken');

                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                }
            });

        $.ajax({
            url: "/julia/create/",
            type: "POST",
            data: { username: $('#twitter-name').val(),
            },
            success : function(json) {
                $('html,body').css('cursor','default');
                alert("Added.");
            },
            error : function(xhr,errmsg,err) {
                $('html,body').css('cursor','default');
                alert("There was a mistake.");
            }
        });

    });

});

function getCookie(name) {

    var cookieValue = null;

    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }

    return cookieValue;

}

function csrfSafeMethod(method) {

    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));

}