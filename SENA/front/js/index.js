document.addEventListener('DOMContentLoaded', function () {

    const mostrarGranja =  () => {

        const cardSection = document.getElementById("i-card-section")

        const granjas = [
             {nombre: "Granja Colombia", producto: "Fresa", img: "fresa.jpg", ubicacion: "Tuta", fecha: new Date(2024, 3, 14 )  }, 
             {nombre: "Granja Avi Boyacá", producto: "Huevos", img:"huevos.jpeg", ubicacion: "Paipa", fecha: new Date(2024, 4, 17 )},
             {nombre: "Leche S.A", producto: "Maiz", img:"maiz.jpeg", ubicacion: "Chocontá", fecha: new Date(2024, 5, 22 )},
             {nombre: "Papa del campo", producto: "Papa", img:"papa.jpeg", ubicacion: "Sogamoso", fecha: new Date(2024, 5, 15 )},
             {nombre: "Granja Cristal", producto: "Durazno", img:"durazno.jpeg", ubicacion: "Toca", fecha: new Date(2024, 8, 4 )},
             {nombre: "Granja Estrella", producto: "Carne", img:"carne.jpeg", ubicacion: "Sotaquirá", fecha: new Date(2024, 6, 1 )}
            ] 

           granjas.forEach( granja => { 
            const verGranja = document.createElement("div")
            verGranja.className = "col-lg-4 col-md-6 col-sm-6 "
            verGranja.innerHTML =  `  
                    <div class="card" style="width: 18rem;">
                        <img src="../img/${granja.img}" class="card-img-top" alt="Productos de Granja ${granja.nombre}">
                        <div class="card-body">
                            <h5 class="card-title">${granja.nombre }</h5>
                            <p class="card-text">${granja.producto}</p>
                            <p class="card-text">${granja.ubicacion}</p>
                            <p class="card-text">${granja.fecha.toLocaleDateString()}</p>
                            <a href="#" class="btn btn-primary">Ver más</a>
                        </div>
                    </div>
            ` 

            cardSection.appendChild(verGranja)

        }) 

    }

    mostrarGranja()

})