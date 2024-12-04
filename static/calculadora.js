$(document).ready(function () {
    let expression = "";
    let memoryValue = null;
    let cy = null

    // Agrega botones de memoria MS y MR
    $(".buttons").append(`
        <button class="button memory" id="ms">MS</button>
        <button class="button memory" id="mr">MR</button>
    `);

    // Manejo del botón negativo
    $("#negativo").click(function () {
        if (
            expression === "" ||
            ["+", "-", "*", "/", "("].includes(expression.slice(-1))
        ) {
            expression += "-";
            $("#display").text(expression);
        }
    });

    function updateTokenValuesTable(tokenValues) {
        const tbody = $("#token-values-table tbody");
        tbody.empty(); // Limpia la tabla actual
        tokenValues.forEach(([token, value]) => {
            tbody.append(`
                <tr>
                    <td>${token}</td>
                    <td>${value}</td>
                </tr>
            `);
        });
    }

    // Actualiza la tabla de frecuencias de tokens
    function updateTokenFrequenciesTable(frequencies) {
        const tbody = $("#token-frequencies-table tbody");
        tbody.empty(); // Limpia la tabla actual
        Object.entries(frequencies).forEach(([token, frequency]) => {
            tbody.append(`
                <tr>
                    <td>${token}</td>
                    <td>${frequency}</td>
                </tr>
            `);
        });
    }

    function renderTree(treeData) {
        if (cy) {
            cy.destroy(); // Destruye el grafo anterior si existe
        }

        cy = cytoscape({
            container: document.getElementById("tree-container"), // Contenedor del árbol
            elements: [...treeData.nodes, ...treeData.edges], // Datos del árbol
            style: [
                {
                    selector: "node",
                    style: {
                        "background-color": "#8ff4a8",
                        "label": "data(label)",
                        "text-valign": "center",
                        "color": "#000000",
                        "width": "60px",
                        "height": "60px",
                        "font-size": "12px",
                        "text-wrap": "wrap",
                    },
                },
                {
                    selector: "edge",
                    style: {
                        "width": 2,
                        "line-color": "#297239",
                        "target-arrow-color": "#297239",
                        "target-arrow-shape": "triangle",
                        "curve-style": "bezier",
                    },
                },
            ],
            layout: {
                name: "breadthfirst", // Diseño en forma de árbol
                directed: true,
                padding: 10,
            },
        });
    }

    $(".button").click(function () {
        const value = $(this).data("value");
        if (value === "C") {
            expression = "";
            $("#display").text("");
            $("#tree-container").empty(); // Limpia el árbol
            $("#token-values-table tbody").empty(); // Limpia la tabla de valores
            $("#token-frequencies-table tbody").empty(); // Limpia la tabla de frecuencias
        } else if (value === "backspace") {
            expression = expression.slice(0, -1);
            $("#display").text(expression);
        } else if (value !== undefined) {
            expression += value;
            $("#display").text(expression);
        }
    });

    // Guardar en memoria
    $("#ms").click(function () {
        if ($("#display").text() !== "") {
            $.ajax({
                url: "/calcular",
                method: "POST",
                contentType: "application/json",
                data: JSON.stringify({ expression }),
                success: function (response) {
                    if (response.valid) {
                        memoryValue = response.result;
                        alert(`Valor ${memoryValue} guardado en memoria`);
                    }
                },
                error: function () {
                    alert("Error al guardar valor en memoria");
                },
            });
        }
    });

    // Recuperar de memoria
    $("#mr").click(function () {
        if (memoryValue !== null) {
            expression += memoryValue.toString();
            $("#display").text(expression);
        } else {
            alert("No hay ningún valor en memoria");
        }
    });

    $("#calcular").click(function () {
        $.ajax({
            url: "/calcular",
            method: "POST",
            contentType: "application/json",
            data: JSON.stringify({ expression }),
            success: function (response) {
                if (response.valid) {
                    // Actualiza la expresión y el display
                    expression = response.result?.toString() || expression;
                    $("#display").text(expression);

                    // Renderiza el árbol
                    renderTree(response.tree);

                    // Actualiza las tablas
                    updateTokenValuesTable(response.token_values);
                    updateTokenFrequenciesTable(response.token_frequencies);
                } else {
                    $("#display").text("Error");
                    $("#tree-container").empty();
                }
            },
            error: function () {
                $("#display").text("Error");
            },
        });
    });

});