function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

actualizarAlbum = () => {

    let idAlbum = document.getElementById("idAlbum").dataset.idalbum;
    let nombreAlbum = document.getElementById("nombreAlbum").value;
    let fechaAlbum = document.getElementById("fechaAlbum").value;
    let generoAlbum = document.getElementById("generoAlbum").value;
    let datos = {
        idAlbum: idAlbum,
        nombreAlbum: nombreAlbum,
        fechaAlbum: fechaAlbum,
        generoAlbum: generoAlbum
    }


    //FETCH
    //FUNCION QUE PERMITE CONECTAR UN SERVIDOR (API) CON TU FRONT
    fetch("http://127.0.0.1:8000/artista/albums/update", {
        method: "POST",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Accept": 'application/json',
            "X-Requested-With": "XMLHttpRequest",
        },
        body: JSON.stringify(datos),
        mode: 'cors',
        cache: 'default',
        credential: 'include'
    })
        .then(
            respuesta => {
                respuesta.text().then(
                    function (data) {

                        if (Boolean(data)) {
                            alert("Cambios hechos correctamente")
                        } else {
                            alert("Ha ocurrido un error")
                        }
                    }
                );

            }
        )
        .catch(
            function (error) {
                alert("Error");
                console.log(error);
            }
        );
}

eliminarAlbum = () => {
    let idAlbum = document.getElementById("idAlbum").dataset.idalbum;

    fetch("http://127.0.0.1:8000/artista/albums/delete", {
        method: "POST",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Accept": 'application/json',
            "X-Requested-With": "XMLHttpRequest",
        },
        body: JSON.stringify(idAlbum),
        mode: 'cors',
        cache: 'default',
        credential: 'include'
    }).then(
        respuesta => {
            respuesta.text().then(
                function (data) {
                    // console.log(data)
                    if (Boolean(data)) {
                        alert("Album borrado correctamente")
                        window.location = "http://127.0.0.1:8000/artista/albums"
                    } else {
                        alert("Ha ocurrido un error")
                    }
                }
            );

        }
    )
        .catch(
            function (error) {
                alert("Error");
                console.log(error);
            }
        );
}