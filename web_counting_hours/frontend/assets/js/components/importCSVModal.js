document.addEventListener("DOMContentLoaded", () => {
    const importCSVButton = document.querySelector(".import-csv");
    const importModal = document.getElementById("import-csv-modal");
    const closeBtn = importModal.querySelector(".close-button");

    importCSVButton.addEventListener("click", () => {
        importModal.style.display = "block";
        loadEmployeeOptions(); // carrega os funcionários no seletor
    });

    closeBtn.addEventListener("click", () => {
        importModal.style.display = "none";
    });

    window.addEventListener("click", (event) => {
        if (event.target === importModal) {
            importModal.style.display = "none";
        }
    });
});

function loadEmployeeOptions() {
    fetch("/api/employees") // você pode ajustar a rota se necessário
        .then(response => response.json())
        .then(data => {
            const select = document.getElementById("employee-select");
            select.innerHTML = '<option value="">Selecione...</option>';
            data.forEach(employee => {
                const option = document.createElement("option");
                option.value = employee.id;
                option.textContent = employee.nome;
                option.dataset.cpf = employee.cpf;
                option.dataset.cargaHoraria = employee.carga_horaria;
                option.dataset.nome = employee.nome;
                select.appendChild(option);
            });

            select.addEventListener("change", (e) => {
                const selected = select.options[select.selectedIndex];
                document.getElementById("employee-name").value = selected.dataset.nome || "";
                document.getElementById("employee-cpf").value = selected.dataset.cpf || "";
                document.getElementById("employee-hours").value = selected.dataset.cargaHoraria || "";
            });
        });
}
