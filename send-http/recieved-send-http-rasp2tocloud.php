#### RECEIVED & SEND DATA HTTP CONNECTION RASP 2 TO CLOUD

#---------------------------------------------------------------------------# 
<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST')
{
  $data = json_decode(file_get_contents("php://input"));
  //print_r($data);
  //echo $data->tanggal;
}
date_default_timezone_set('Asia/Jakarta');
//FUNGSI CAPTURE DATA KE REMOTE DATABASE
// MEMBUAT OBJEK DATABASE
        $dbhost = "192.168.1.73";
        $database ="**********”;
        $dbuser = "*********";
        $dbpass = "**********";
        $con = mysql_connect($dbhost,$dbuser,$dbpass);
        if(!$con)
        {die ("Koneksi gagal");}	
	
		$querysoc = "SELECT Tegangan as Vc1, SOC, SOC_Peukert as SOCcell,
				ABS(Tegangan - (".$_REQUEST['Vcell'].")) as diffs
				FROM `smartgrid_tf`.`SPB_cell_init_float` Where 1  
				ORDER BY diffs ASC limit 1";
			$resultss = mysql_query($querysoc);
			$rowss = mysql_fetch_row($resultss);
	$soccell = $rowss[2]*100;
			
	$query = "REPLACE INTO `smartgrid_tf`.`SPB_cell_datapengukuran` (`id`, `datetime`, `SPB_Lm_id`, `SPB_Lm_ver`, `Imod`, `Tmod`, `SPB_Cell_id`, `SPB_Cell_ver`, `Vcell`, `Tcell`, `IntRcell`, `SOCcell`, `SOHcell`) VALUES (NULL, '".$_REQUEST['tanggal']."', '".$_REQUEST['SPB_Lm_id']."', '".$_REQUEST['SPB_Lm_ver']."', '".$_REQUEST['Imod']."', '".$_REQUEST['Tmod']."', '".$_REQUEST['SPB_Cell_id']."', '".$_REQUEST['SPB_Cell_ver']."', '".$_REQUEST['Vcell']."', '".$_REQUEST['Tcell']."', '".$_REQUEST['IntRcell']."', '".$soccell."', '".$_REQUEST['SOHcell']."')";
		echo $result = mysql_query($query);


	//Kirim ke cloud via proxy ITB
$data_string = json_encode($_REQUEST);                                                                                   
$ch = curl_init('http://198.61.224.73/capture/database/SPB-put-json.php');   
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");                                                                     
curl_setopt($ch, CURLOPT_POSTFIELDS, $data_string);                                                                  
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);                                                                      
curl_setopt($ch, CURLOPT_HTTPHEADER, array(                                                                          
    'Content-Type: application/json',                                                                                
    'Content-Length: ' . strlen($data_string))                                                                       
);                                                                                                                   
// Perform the request, and save content to $result
$resultscurl = curl_exec($ch);
	echo $resultscurl;
?>