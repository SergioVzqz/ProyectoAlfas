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

agregarCancion = () => {
    let nombreCancion = document.getElementById("nombreCancion").value;
    let duracionCancion = document.getElementById("duracionCancion").value;
    let autorCancion = document.getElementById("autorCancion").value;
    let idAlbum = document.getElementById("albumCancion").dataset.idalbum;
    let archivoCancion = document.getElementById("archivoCancion").files[0];


    let formData = new FormData();
    formData.append("csrfmiddlewaretoken", getCookie("csrftoken"));
    formData.append("nombreCancion", nombreCancion);
    formData.append("duracionCancion", duracionCancion);
    formData.append("autorCancion", autorCancion);
    formData.append("idAlbum", idAlbum);
    formData.append("archivoCancion", archivoCancion);


    //AJAX CON JQUERY
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/artista/cancion/add",
        data: formData,
        //Unicos para este caso
        processData: false, //No procese la informacion, simplemente que la envie
        contentType: false, //No envie el contentType
        success: function (data) {
            console.log(data)
            if (Boolean(data)) {
                $("#modalAdd").modal("hide");
                $("#modalExito").modal("show");
                $('#modalExito').on('hidden.bs.modal', function (e) {
                    location.reload();
                })
            }
        },
        error: function (data) {
            $("#modalAdd").modal("hide");
            $("#modalError").modal("show");
        }

    })
}


eliminarCancion = (elemento) => {
    let idCancion = elemento.getAttribute("data-id")
    let token = getCookie("csrftoken")

    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/artista/cancion/delete",
        data: {
            csrfmiddlewaretoken: token,
            idCancion: idCancion
        },
        success: function (data) {
            $("#modalSongD").modal("hide");
            $('#modalSongD').on('hidden.bs.modal', function (e) {
                location.reload();
            })
        },
        error: function (data) {
            console.log(data);
            alert("Ha ucorrido un error")
        }

    })
}



actualizarCancion = (elemento) => {
    let nombreCancion = document.getElementById("nombreCancionE").value;
    let duracionCancion = document.getElementById("duracionCancionE").value;
    let autorCancion = document.getElementById("autorCancionE").value;
    let idCancion = elemento.getAttribute("data-id")
    let token = getCookie("csrftoken")
    console.log(nombreCancion, duracionCancion, autorCancion, idCancion)

    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/artista/albums/nuevo/add",
        data: {
            csrfmiddlewaretoken: token,
            nombreCancion: nombreCancion,
            duracionCancion: duracionCancion,
            autorCancion: autorCancion,
            idCancion: idCancion
        },
        success: function (data) {
            console.log(data)
            $('#modalSongE').on('hidden.bs.modal', function (e) {
                location.reload();
            })
        },
        error: function (data) {
            console.log(data);
            // alert("Ha ucorrido un error")
        }

    })

}


agregarAlbum = () => {
    let nombreAlbum = document.getElementById("nombreAlbum").value;
    let fechaAlbum = document.getElementById("fechaAlbum").value;
    let disqueraAlbum = document.getElementById("disqueraAlbum").value;
    let generoAlbum = document.getElementById("generoAlbum").value;
    let fotoAlbum = document.getElementById("imagenAlbum");

    let formData = new FormData();
    formData.append("csrfmiddlewaretoken", getCookie("csrftoken"));
    formData.append("nombreAlbum", nombreAlbum);
    formData.append("fechaAlbum", fechaAlbum);
    formData.append("disqueraAlbum", disqueraAlbum);
    formData.append("generoAlbum", generoAlbum);
    formData.append("fotoAlbum", fotoAlbum.files[0]);

    let numeroCanciones = 0;
    $.each($("#cancionesAlbum"), function (i, obj) {
        $.each(obj.files, function (j, file) {
            numeroCanciones = j;
            formData.append('cancion[' + j + ']', file);
        })
    })
    formData.append("numeroCanciones", numeroCanciones.toString());

    //AJAX CON JQUERY
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/artista/albums/nuevo/add",
        data: formData,
        //Unicos para este caso
        processData: false, //No procese la informacion, simplemente que la envie
        contentType: false, //No envie el contentType
        success: function (data) {
            $("#modalExito").modal("show");
            $('#modalExito').on('hidden.bs.modal', function (e) {
                location.reload();
            })
        },
        error: function (data) {
            
        }

    })
}

buscarCancion = () =>{
    let texto = document.getElementById("search").value
    let token = getCookie("csrftoken")
    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/reproduccion/busqueda',
        data:{
            csrfmiddlewaretoken: token,
            texto: texto
        },
        success: function(data){
            console.log(data);
        },
        error: function(data){
            console.log(data);
        }
    })
}