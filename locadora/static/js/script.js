$(document).ready(function(){

   var deleteBtn = $('.delet-btn');

   $(deleteBtn).on('click', funcion(e){
  
    e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Quer excluir realmente?');

        if(result){
            window.location.href = delLink;
        }


   });

});