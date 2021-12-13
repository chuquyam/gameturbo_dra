(function(win,doc){

    'use strict';

    alert('Bem vindo ao gameturbo Locadora');
    
    if(doc.querySelector('.btnDel')){
        let btnDel = doc.querySelectorAll(' .btnDel');
        for(let i=0; i < btnDel.length; i++){
            btnDel[i].addEventListener('click', function(event){

                if(confirm('Deseja mesmo apagar este registro?')){
                    return true;
                }else{
                    event.preventDefault();
                }
            })

        }

    }

}) (window,document);

$(document).ready(function() {
    $(".dropdown-toggle").dropdown();
});