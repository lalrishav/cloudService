<!DOCTYPE>
<head>
	<title>Welcome</title>
	<style type="text/css">
		#side-panel{
			float: left;
			border-style: solid;
			border-left:5px dotted red;
			border-right:5px dotted blue;
			border-bottom:5px solid orange;
			border-top:5px solid pink;
			border-radius: 30px;
   			background-color: black;
			width: 250px;
			height: 470px;
			padding: 20px;
		}

		#right-panel{
			float: right;
			border-style: solid;
			border:1px solid red;
			border-radius: 900px;
			width: 950px;
			height: 440px;
			padding:30px;
			background-color: black
		}
		#aboutSaas{
		
			border-style: solid;
			border-top:4px dotted red;
			border-bottom:4px dotted green;
			border-left: 4px solid yellow;
			border-right: 4px solid blue;
			border-radius: 900px;
			width: 940px;
			height: 400px;
			padding-top: 35px;
			background-color: white
		}
	</style>
	<script type="text/javascript">

		function display(string){
			//str = "about" + string
			//document.getElementById(str).style.display = "block";

		}
	</script>

</head>
<body>
	<center><h1 style="color:red">Take a look Over our Services</h1></center>
	<div id="side-panel">
		<h2 id="saas" onmouseover="display('Saas')"><input type="radio"> &nbsp&nbspSoftware as a &nbsp&nbsp&nbsp&nbsp&nbsp&nbspService(SAAS)</h2>
		<h2 id="staas" onmouseover="display('Staas')"><input type="radio"> &nbsp&nbspStorage as a &nbsp&nbsp&nbsp&nbsp&nbsp&nbspService(StAAS)</h2>
		<h2 id="iaas" onmouseover="display('Iaas')"><input type="radio"> &nbsp&nbspInfrastructure &nbsp&nbsp&nbsp&nbsp&nbsp  as a Service</h2>

	</div>
	<div id="right-panel">
		<div id="aboutSaas" style="display:block">
			<center><h2>Software as a Service</h2>
				<p>
					Content about SAAS
				</p>

			</center>
		</div>
		<div id="aboutStaas" style="display:none">
			<center><h2>Software as a Service</h2>
				<p>
					Content about StAAS
				</p>

			</center>
		</div>
		<div id="aboutIaas" style="display:none">
			<center><h2>Software as a Service</h2>
				<p>
					Content about IAAS
				</p>

			</center>
		</div>
	</div>
</body>