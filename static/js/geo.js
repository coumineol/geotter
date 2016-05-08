var utc = new Date().toJSON().slice(0,10);

$( document ).ready(function() {

    $('html,body').css('cursor','default');

    $('#grant-permission').on('click', function() {

        $('html,body').css('cursor','progress');

        function getLocation() {

            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(saveLocation);
            } else {
                $('html,body').css('cursor','default');
                alert("Couldn't get your location.");
            }

        }

        function saveLocation(position) {

            var myLatitude = position.coords.latitude.toString();
            var myLongitude = position.coords.longitude.toString();

            console.log(myLatitude);

            $.ajaxSetup({
                beforeSend: function(xhr, settings) {
                    csrftoken = getCookie('csrftoken');

                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                }
            });

            $.ajax({
                url: "/geo/create/detect/",
                type: "POST",
                data: { latitude: myLatitude,
                        longitude: myLongitude,
                },
                success : function(json) {
                    $('#location-list').append('<li>Date: ' + utc + ' - Latitude: ' + myLatitude + ' - Longitude: ' + myLongitude + '</li>');
                    $('html,body').css('cursor','default');
                    alert("Added.");
                },
                error : function(xhr,errmsg,err) {
                    console.log(err);
                    $('html,body').css('cursor','default');
                }
            });

        }

        getLocation();

        $('html,body').css('cursor','default');

    });

    $('#locate-city').on('click', function() {

        $('html,body').css('cursor','progress');

        var myCity = $("#city-name").val()

        $.ajaxSetup({
                beforeSend: function(xhr, settings) {
                    csrftoken = getCookie('csrftoken');

                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                }
            });

        $.ajax({
            url: "/geo/create/city/",
            type: "POST",
            data: { getCity: myCity },
            success : function(json) {
                $('html,body').css('cursor','default');
                $('#location-list').append('<li>Date: ' + json['date'].slice(0,10) + ' - Latitude: ' + json['latitude'] + ' - Longitude: ' + json['longitude'] + '</li>');
                alert("Added.");
            },
            error : function(xhr,errmsg,err) {
                $('html,body').css('cursor','default');
                alert("There was an error.");
            }
        });

        $('html,body').css('cursor','default');

    });

    $('#locate-country').on('click', function() {

        console.log("tiklandi");

        $('html,body').css('cursor','progress');

        var myCountry = $("#country-name").val()
        var myZip = $("#zip-code").val()

        $.ajaxSetup({
                beforeSend: function(xhr, settings) {
                    csrftoken = getCookie('csrftoken');

                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                }
            });

        $.ajax({
            url: "/geo/create/country/",
            type: "POST",
            data: { getCountry: myCountry,
                    getZip: myZip
            },
            success : function(json) {
                $('html,body').css('cursor','default');
                $('#location-list').append('<li>Date: ' + json['date'].slice(0,10) + ' - Latitude: ' + json['latitude'] + ' - Longitude: ' + json['longitude'] + '</li>');
                alert("Added.");
            },
            error : function(xhr,errmsg,err) {
                $('html,body').css('cursor','default');
                alert("There was an error.");
            }
        });

        $('html,body').css('cursor','default');

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