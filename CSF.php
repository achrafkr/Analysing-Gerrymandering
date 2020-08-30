<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1"/>
        <link rel="stylesheet" href="Style.css"/>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">

        <title>Gerrymandering</title>
    </head>
 
    <body>
        <header>
            <?php include("navigation.php"); ?>            
        </header>  
               
        <div>
            <section class="corps"> 
                <br>
                <p>
                    Le <strong>Flux de raccourcissement géométrique</strong> ou <strong>Curve shortening flow</strong> est une technique utilisée pour déterminer un gerrymander à travers d’une approche géométrique. L’objectif de cette technique est de raccourcir en utilisant les algorithmes appropriés  la courbe fermée composée par les limites d'une circonscription, pour ensuite tracer l'évolution de la compacité pour une circonscription donnée. Finalement l'étude de son comportement (comment elle rétrécit) et l’allure de la courbe d'évolution permet de donner un verdict sur la légalité de la circonscription. 
                </p>
                <p>
                    Elle est basée sur la technique mathématique qui porte le même nom, le <i>Curve shortening flow</i>. Le principe de cette technique mathématique est d’étudier le comportement d’une courbe fermée lorsqu’elle rétrécit. Les courbes étudiées vérifient l’équation <span class="cmath"> ` (∂γ) / (∂t)=  (∂^2 γ) / (∂s^2 )` </span>: c’est un cas géométrique non linéaire de l’équation de la chaleur. Ainsi, la courbe évolue en fonction de la courbure de l’arc s en chaque point de la courbe.
                </p>
               
            </section>
            
            <section class="corps">
                <img src="Pics/csf.png" class="csf">
            </section>

        </div>
            <br>
            <br>
            <br>

        <footer class="card-footer bg-dark">
           <p class="footercontent">Achraf KRIM - Tous droits réservés</p>
        </footer>
    
    </body>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
     <script async="true" src="https://cdn.jsdelivr.net/npm/mathjax@2/MathJax.js?config=AM_CHTML"> </script>
</html>