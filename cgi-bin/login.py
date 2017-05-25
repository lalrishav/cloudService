#!/usr/bin/python2

import cgi
form = cgi.FieldStorage()
password = "redhat"
print "Content-type: text/html\n"
print ""

web  = '''
				<html>
		<head>
<title>Welcome</title>
<style type="text/css">
	#side-panel{
		background: url(/static/cloud2.jpg) repeat;
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
		background: url(/static/cloud.jpg) repeat;
		position: absolute;
		border-style: solid;
		left: 410px;
		border-bottom: 4px solid yellow;
		border-top: 4px solid blue;
		border-left:4px dotted red;
		border-right:4px dotted green;
		border-radius: 900px;
		width: 840px;
		height: 440px;
		padding:30px;
		
	}
	
	#submit{
		position: absolute;
		bottom: 550px;
		left: 1200px;
		height: 30px;
		background-color: green;
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
<form action="service.py" method="post">
<div id="side-panel">
	<h2 id="saas" onmouseover="display('Saas')"><input type="radio" name="service" value="saas" onclick="location.href='/services/saas.html'"> &nbsp&nbspSoftware as a &nbsp&nbsp&nbsp&nbsp&nbsp&nbspService(SAAS)</h2>
	<h2 id="staas" onmouseover="display('Staas')"><input type="radio" name="service" value="staas" onclick="location.href='services/staas.html'"> &nbsp&nbspStorage as a &nbsp&nbsp&nbsp&nbsp&nbsp&nbspService(StAAS)</h2>
	<h2 id="iaas" onmouseover="display('Iaas')"><input type="radio" name"service" value="iaas" onclick="location.href='services/iaas.py'"> &nbsp&nbspInfrastructure &nbsp&nbsp&nbsp&nbsp&nbsp  as a Service</h2>
</div>
<input type="submit" id="submit" value="Proceed">
</form>
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
		</html>
	'''

error = '''
	<html>
		<script>alert("wrong username password")</script>
	</html>
	'''







if not form:
	print "<H1>You need to login first to access this page</H1>"
else:
	if form["password"].value == password and form["user"].value!="":
		print web
	else:
		print error

