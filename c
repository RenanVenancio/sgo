[1mdiff --git a/sistema/templates/sistema/chamados/editarchamado.html b/sistema/templates/sistema/chamados/editarchamado.html[m
[1mindex e09c809..459501f 100755[m
[1m--- a/sistema/templates/sistema/chamados/editarchamado.html[m
[1m+++ b/sistema/templates/sistema/chamados/editarchamado.html[m
[36m@@ -153,7 +153,7 @@[m
                                         <div class="">[m
                                             {{form.apartamento|add_class:"form-control selectpicker"|attr:"id=apartamento_id data-live-search=true data-width=100%"}}[m
                                             {{ form.apartamento.errors }}[m
[31m-                                            <p id="garantiaApto"></p>[m
[32m+[m[32m                                            <p id="garantiaApto"> Garantia: {{ view.garantia }} </p>[m[41m[m
 [m
                                         </div>[m
                                     </div>[m
[36m@@ -305,7 +305,19 @@[m
             }[m
        });[m
 [m
[32m+[m[32m       $("#apartamento_id").change(function() {[m[41m[m
[32m+[m[32m            var dado = $(this).find(':selected').attr('garantia');[m[41m[m
[32m+[m[32m            $("#garantiaApto").text('Garantia: ' + dado);[m[41m[m
[32m+[m[32m        });[m[41m[m
[32m+[m[41m[m
         $( document ).ready(function() {[m
[32m+[m[32m            let statusAreaComum = $('.check-area').is(':checked'); //Verificando se possui area comum[m[41m[m
[32m+[m[32m            if(statusAreaComum == true){[m[41m[m
[32m+[m[32m                $(".menu-area").fadeIn();[m[41m[m
[32m+[m[32m            }else{[m[41m[m
[32m+[m[32m                $(".menu-area").fadeOut();[m[41m[m
[32m+[m[32m            }[m[41m[m
[32m+[m[41m[m
             var selectbox = $('#apartamento_id');[m
             selectbox.find('option').css('display', 'none');[m
             $('.selectpicker').selectpicker('refresh');  //Atualiza os selectpickers[m
