<?php
include('dbconnect.php');
if ($conn->connect_error) {
    die('Connect Error (' . $conn->connect_errno . ') '. $conn->connect_error);
}
$getstate = $conn->query('SELECT state from ivanOIGswing');
while($array[] = $getstate->fetch_object());
array_pop($array);
?>
<?php
if (isset($_POST['submit'])){
    include ('dbconnect.php');
    $ustate = $_POST['state'];
    $job_loss = "SELECT job_loss FROM ivanOIGswing WHERE state = '$ustate' LIMIT 1";
    $q_job_loss = mysqli_query($conn, $job_loss);
    $jl = mysqli_fetch_array($q_job_loss);
    $rev_loss = "SELECT revenue_lost FROM ivanOIGswing WHERE state = '$ustate' LIMIT 1";
    $q_rev_loss = mysqli_query($conn, $rev_loss);
    $rl = mysqli_fetch_array($q_rev_loss);
    $margin_drop = "SELECT median_operating_margin FROM ivanOIGswing WHERE state = '$ustate' LIMIT 1";
    $q_margin_drop = mysqli_query($conn, $margin_drop);
    $md = mysqli_fetch_array($q_margin_drop);
}
?>
<html>
<head>
<link rel="stylesheet" type="text/css" href="css/style.css"/>
<link href="css/lightbox.css" rel="stylesheet"/>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
<script src="js/lightbox.min.js"></script>
</head>
<body>
<div id="main">
<H1>IMPACT TO CRITICAL ACCESS HOSPITAL REIMBURSEMENTS</H1>
<p>A RECENT OIG REPORT RECOMMENDS CUTTING CRITICAL ACCESS HOSPITAL SWINGBED REIMBURSEMENTS.</p>
<p>iVantage modeled alternative reimbursements suggested by OIG for every CAH in the country.</p>
</div>
<div id="smain">
<p><span class="largefont">National Impact:</span></p>
<p id="t_revenue"><span class="largefont"> $1.2 BILLION </span> IN LOST REVENUE PER YEAR<br/><a href="img/m_revenue.PNG" data-lightbox="image-1" data-title="impact on revenue">(view impact map)</a></p>
<p id="t_jobs">NEARLY <span class="largefont"> 25K LOST JOBS </span> <br/><a href="img/m_jobs.PNG" data-lightbox="image-2" data-title="impact on hospital jobs">(view impact map)</a></p>
<p id="t_margin">A<span class="largefont"> 5 PERCENTAGE POINT DROP </span> IN THE MEDIAN OPERATING MARGIN FOR CRITICAL ACCESS HOSPITALS.<br/><a href="img/m_margin.PNG" data-lightbox="image-3" data-title="impact on operating margin">(view impact map)</a></p>
</div>
<br/>
<div id="menu">
<p>HOW COULD YOUR STATE BE IMPACTED?</p>
<div id="uselect">
<form action="oigswingbedanalysis.php#impact" method="post">
<select name="state" id="state">
<?php foreach($array as $option) : ?>
    <option value="<?php echo $option->state; ?>"><?php echo $option->state; ?></option>
<?php endforeach; ?>   
</select>
<script type="text/javascript">
   $("#state").val("<?php echo $_POST['state'];?>");
</script>
<input id="submitter" type="submit" name="submit" value="SHOW IMPACT"/>
</form>
</div> 
</div>
<div id="container">
<div id="revenue">
<?php 
if ($_POST['state']==""){
echo "";
} else {
echo $rl['revenue_lost']; 
}
?>
</div>
<div id="jobs">
<?php 
if ($_POST['state']==""){
echo "";
} else {
echo number_format($jl['job_loss'],0); 
}
?>
</div>
<div id="margin">
<?php 
if ($_POST['state']==""){
echo "";
} else {
echo $md['median_operating_margin']; 
}
?>
</div>
</div>
<div id="impact">
<div id="b_revenue"><img style="height:auto; width:auto; max-width:175px; max-height:175px;" src="assets/money.PNG"/><br/>million in lost revenue</div>
<div id="b_jobs"><img style="height:auto; width:auto; max-width:250px; max-height:250px;" src="assets/bc.PNG"/>jobs lost</div>
<div id="b_margin"><img style="height:auto; width:auto; max-width:175px; max-height:175px;" src="assets/drop.PNG"/><br/>percentage point drop <br/>in operating margin</div>
</div>
<div id="spacer">How strong or vulnerable is your hospital? Call today for a brief review. 1-207-518-6705.</div>
<a id="anch"></a>
<div id="foot">&copy; 2014. iVantage Health Analytics</div>
<img id="logo" style="height:auto; width:auto; max-width:250px; max-height:40px;" src="assets/ivant.PNG"/>
</body>
</html>