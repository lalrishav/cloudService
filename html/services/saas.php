<html>
<head>
	
	<style type="text/css">
		body{
			background: url(/static/hdbg.jpg) repeat;
		}
		select{
			height: 50px;
			width: 200px;
			text-align: center;
		}
		table {
		    font-family: arial, sans-serif;
		    border-collapse: collapse;
		    width: 100%;
		}

		td, th {
		    border: 1px solid #dddddd;
		    text-align: left;
		    padding: 8px;
		}

		tr:nth-child(even) {
		    background-color: #dddddd;
		}
		tr:nth-child(odd) {
		    background-color: black;
		}
		#t{
			position: absolute;
			left: 300px;
		}
		#left{

		}
	</style>

	<script type="text/javascript">
		var a = new Array(4)
		for(var i=0;i<4;i++){
			a[i] = i+1;
		}
		function tooglediv(){
			var p = document.getElementById('a').value;
			console.log(p)
			for(i=0;i<4;i++){
				if(i+1==p){
					document.getElementById(p).style.display = "block";
				}
				else{
					console.log(4+"a")
					document.getElementById((i+1)).style.display = "none"
				}
			}

		}
	</script>

</head>
<body>
	<div id="left">
		<h1><span style="color:blue">Software List</span></h1>
		<select onchange="tooglediv()" id="a">
			  <option value="1">Microsoft Windows</option>
			  <option value="2">Linuix</option>
			  <option value="3">MaC</option>
			  <option value="4">Android</option>
		</select><br><br><br>
	</div>
		<center id="t">
			<div id="1" style="display:block">
			<table>
				  <tr>
				    <td><a href="/cgi-bin/abc.py?val=firefox">Firefox</a></td>
				    <td><a href="/cgi-bin/abc.py?val=gedit">Gedit</td>
				    <td>Virt-Manager</td>
				    <td>VLC</td>
				    <td>Flash PLayer</td>
				    <td>Tiger VNC</td>
				  </tr>
				  
				  <tr>
				    <td>Google-Chrome</td>
				    <td>Safari</td>
				    <td></td>
				    <td>Alfreds Futterkiste</td>
				    <td>Maria Anders</td>
				    <td>Germany</td>
				  </tr>
				  <tr>
				    <td>Laughing Bacchus Winecellars</td>
				    <td>Yoshi Tannamuri</td>
				    <td>Canada</td>
				    <td>Alfreds Futterkiste</td>
				    <td>Maria Anders</td>
				    <td>Germany</td>
				  </tr>
				  
			</table>
		</div>
	</center>
		<div id="2" style="display:none">
			li
		</div>
		<div id="3" style="display:none">
			ma
		</div>
		<div id="4" style="display:none">
			and
		</div>
	</div>
<body>
</html>