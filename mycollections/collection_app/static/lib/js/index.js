  $('#enviar').hide();
  $('#btn_enviar').click(function () {
          $('#enviar').show('slow');
          $('#btn_enviar').hide('slow');
  });


   $('body').show();
   
   $("#conteudo").hide();//esconde o conteudo ate carregar tudo
   $('.version').text(NProgress.version);
   NProgress.start();
   setTimeout(function() {
     NProgress.done();
     $("#conteudo").show();//mostra o conteudo da pagina ao terminar de carregar
     $('.fade').removeClass('out');
   }, 1000);
//aqui é para chamar atraves de botoes
   $("#b-0").click(function() { NProgress.start(); });
   $("#b-40").click(function() { NProgress.set(0.4); });
   $("#b-inc").click(function() { NProgress.inc(); });
   $("#b-100").click(function() { NProgress.done(); });