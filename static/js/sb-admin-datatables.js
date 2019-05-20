// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('.dataTable').DataTable({
    responsive: true,
    destroy:true,
    // Tradução para pt-br dos controles do DataTable
    "language":{
      "sEmptyTable": "Nenhum registro encontrado",
      "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
      "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
      "sInfoFiltered": "(Filtrados de _MAX_ registros)",
      "sInfoPostFix": "",
      "sInfoThousands": ".",
      "sLengthMenu": "_MENU_ resultados por página",
      "sLoadingRecords": "Carregando...",
      "sProcessing": "Processando...",
      "sZeroRecords": "Nenhum registro encontrado",
      "sSearch": "Pesquisar",
      "oPaginate": {
          "sNext": ">",
          "sPrevious": "<",
          "sFirst": "Primeiro",
          "sLast": "Último"
      },
      buttons: {
        copyTitle: 'Copiado',
        copySuccess: {
            _: '%d linhas copiadas',
            1: '1 linha copiada'
        }
      },
      "oAria": {
          "sSortAscending": ": Ordenar colunas de forma ascendente",
          "sSortDescending": ": Ordenar colunas de forma descendente"
      }
    },
    // Reordenação de layout e tradução de botões DataTable
    dom:"<'row'<'col-sm-5'B><'col-sm-7'f>>" +
			"<'row'<'col-sm-12'tr>>" +
			"<'row'<'col-sm-12 col-md-5'i><'col-sm-12 col-md-7'p>>",
    buttons: [
      {
        text: 'Imprimir',
        extend: 'print',
        className: 'btn btn-primary waves-effect',
        title: '',
      },
      {
        text: 'Copiar',
        extend: 'copyHtml5',
        className: 'btn btn-primary waves-effect',
      },
      {
        text: 'Excel',
        extend: 'excelHtml5',
        className: 'btn btn-primary waves-effect',
      },
    ]
    

  });
});
