<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Documentação e análise de dados de testes de antibiograma</title>
</head>
<body>
  <h1>Documentação e análise de dados de testes de antibiograma</h1>

  <form action="/teste" method="post">
    <input type="text" name="data" placeholder="Data">
    <input type="time" name="hora" placeholder="Hora">
    <input type="text" name="local" placeholder="Local">
    <input type="text" name="tipo_amostra" placeholder="Tipo de amostra">
    <input type="text" name="antibiotico" placeholder="Antibiótico">
    <input type="number" name="concentracao" placeholder="Concentração">
    <input type="number" name="crescimento" placeholder="Crescimento">
    <input type="submit" value="Enviar">
  </form>

  <div id="graficos"></div>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/chart.js/3.7.0/chart.min.js"></script>

  <script>
    $(document).ready(function() {
      // Obtém os dados do formulário
      var data = $("#teste").serializeArray();

      // Cria um objeto JSON com os dados
      var dados = JSON.stringify(data);

      // Carrega os dados no gráfico
      var ctx = document.getElementById("graficos").getContext("2d");
      var chart = new Chart(ctx, {
        type: "line",
        data: {
          labels: data.map(function(item) {
            return item.data;
          }),
          datasets: [{
            label: "Crescimento de bactérias",
            data: data.map(function(item) {
              return item.value;
            }),
            backgroundColor: "rgba(255, 0, 0, 0.2)",
            borderColor: "rgb(255, 0, 0)",
            borderWidth: 1
          }]
        },
        options: {
          title: "Crescimento de bactérias em função do tempo",
          scales: {
            y: {
              min: 0,
              max: 100
            }
          }
        }
      });

      // Adiciona opções de filtro
      var filter = document.querySelector(".filter");
      filter.addEventListener("change", function() {
        var filtro = filter.value;
        var dadosFiltrados = dados.filter(function(item) {
          return item[filtro] === true;
        });
        chart.data.datasets[0].data = dadosFiltrados.map(function(item) {
          return item.value;
        });
        chart.update();
      });

      // Adiciona botões de exportação
      var exportarCSV = document.querySelector(".exportar-csv");
      exportarCSV.addEventListener("click", function() {
        var dadosExportados = JSON.parse(dados);
        window.location.href = "/exportar/csv?dados=" + encodeURIComponent(JSON.stringify(dadosExportados));
      });
      var exportarPDF = document.querySelector(".exportar-pdf");
      exportarPDF.addEventListener("click", function() {
        var dadosExportados = JSON.parse(dados);
        window.location.href = "/exportar/pdf?dados=" + encodeURIComponent(JSON.stringify(dadosExportados));
      });
    });
  </script>
