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

    selectFilter($("#id_empreendimento"), $("#id_bloco"), $("#idapartamento"));
    selectFilter($("#id_bloco"), $("#idapartamento"), $(null));


  }

});





