// Filtro para popular selects de cadastro de chamadas

function selectFilter($s1, $s2, $s3) {

  $s2.children('option:gt(0)').hide();
  $s1.change(function() {
      $s2.children('option').hide();
      $s2.val(null);
      $s3.children('option').hide();
      $s3.val(null);
      $s2.children("option[id=" + $(this).val() + "]").show();

      $('.selectpicker').selectpicker('refresh');  //Atualiza os selectpickers
  }
)}

// chamada de métodos apenas para cadastro de cadastro de chamadas
$(document).ready(function() {
  if (cadastrar == true){

    selectFilter($("#id_empreendimento"), $("#id_bloco"), $("#id_apartamento"));
    selectFilter($("#id_bloco"), $("#id_apartamento"), $(null));
  }


table = $('table').DataTable({
    destroy: true,
    select: true,

    language: {
        last:       "Dernier",
        search:         "Buscar:",
        zeroRecords:    "Não foi encontrado nenhum registro",
        emptyTable:     "Não há nehum dado para exibir",

        paginate: {
            first:      "Primeiro",
            previous:   "Anterior",
            next:       "Próximo",
            last:       "Último"
        },
    }



});





