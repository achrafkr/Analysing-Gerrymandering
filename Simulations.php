<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
        <script type="text/javascript" src="Simulations.js"></script>
        <link rel="stylesheet" href="Style.css"/>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
        <title>Simulations</title>
    </head>
 
    <body >

	    <?php include("navigation.php"); ?>
		    <div class="p-3 mb-2" style="background-color: gray">
		    	<h1 class="title">Curve Shortening Flow - Simulations</h1>

		    	<form class="form-inline">	
					<div class="form-group col-md-6 mb-2">
						<div class="col-md-5 mb-2">
							
							<select class="custom-select mr-2 " id="departement">
							    <option value="">--Veuillez choisir un département--</option>
							    <option value="09">09 - Ariège</option>
							    <option value="11">11 - Aude</option>
							    <option value="12">12 - Aveyron</option>
							    <option value="30">30 - Gard</option>
							    <option value="31">31 - Haute-Garonne</option>
							    <option value="32">32 - Gers</option>
							    <option value="34">34 - Hérault</option>
							    <option value="46">46 - Lot</option>
							    <option value="48">48 - Lozère</option>
							    <option value="66">66 - Pyrénées-Orientales</option>
							    <option value="81">81 - Tarn</option>
							    <option value="82">82 - Tarn-et-Garonne</option>
							</select>

						</div>
						
						<div class="col-md-5 mb-2 d-flex" style="margin-left: 15px">
							
							<select class="custom-select mr-2" id="circonscription">
							    <option value="">--Veuillez choisir une circonscription--</option>
							    <option value="1">1</option>
							    <option value="2">2</option>
							    <option value="3">3</option>
							    <option value="4">4</option>
							    <option value="5">5</option>
							    <option value="6">6</option>
							    <option value="7">7</option>
							    <option value="8">8</option>
							    <option value="9">9</option>
							    <option value="10">10</option>

							</select>

							<input type="button" class="btn btn-info" name="affichage" value="Valider" onclick="simulations();" />	

						</div>

						</div>										
					</div>
				</form>

					
					<div class="container">
						<img id="image" class="image" src="">
						<video id="animation" class="animation" width="500" height="400" controls="controls"><source src="" type="video/mp4" />
					</div>
				</div>
			</div>
			
	</body>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
	<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
    
</html>