####RECEIVED DATA HTTP CONNECTION CLOUD####

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
        $dbhost = "127.0.0.1";
        $database ="*********";
        $dbuser = "**********";
        $dbpass = "***********";
        $con = mysql_connect($dbhost,$dbuser,$dbpass);
        if(!$con)
        {die ("Koneksi gagal");}
        //mysql_select_db($database,$con) or die ("database tidak ditemukan");
        //EKSEKUSI FUNGSI
        //$query = "REPLACE INTO `emon_tf`.`datapengukuran` (`id`, `timestamp`, `meter_id`, `quality`, `A`, `A1`, `A2`, `A3`, `VLL`, `VLN`, `V12`, `V23`, `V31`, `V1`, $
        //$result = mysql_query($query);
        $query = "REPLACE INTO `smartgrid_tf`.`SPB_cell_datapengukuran` (`id`, `datetime`, `SPB_Lm_id`, `SPB_Lm_ver`, `Imod`, `Tmod`, `SPB_Cell_id`, `SPB_Cell_ver`, `Vcell`, `Tcell`, `IntRcell`, `SOCcell`, `SOHcell`) VALUES (NULL, '".$data->tanggal."', '".$data->SPB_Lm_id."', '".$data->SPB_Lm_ver."', '".$data->Imod."', '".$data->Tmod."', '".$data->SPB_Cell_id."', '".$data->SPB_Cell_ver."', '".$data->Vcell."', '".$data->Tcell."', '".$data->IntRcell."', '".$data->SOCcell."', '".$data->SOHcell."')";
        //$query = "REPLACE INTO `smartgrid_tf`.`SPB_cell_datapengukuran` (`id`, `datetime`, `SPB_Lm_id`, `SPB_Lm_ver`, `Imod`, `Tmod`, `SPB_Cell_id`, `SPB_Cell_ver`, `Vcell`, `Tcell`, `IntRcell`, `SOCcell`, `SOHcell`) VALUES (NULL, '".$_REQUEST['tanggal']."', '".$_REQUEST['SPB_Lm_id']."', '".$_REQUEST['SPB_Lm_ver']."', '".$_REQUEST['Imod']."', '".$_REQUEST['Tmod']."', '".$_REQUEST['SPB_Cell_id']."', '".$_REQUEST['SPB_Cell_ver']."', '".$_REQUEST['Vcell']."', '".$_REQUEST['Tcell']."', '".$_REQUEST['IntRcell']."', '".$_REQUEST['SOCcell']."', '".$_REQUEST['SOHcell']."')";
        echo $result = mysql_query($query);


/*        //Kirim ke cloud via proxy ITB
$data_string = json_encode($data);
$ch = curl_init('http://eng-cloud.com/capture/database/json.php');
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
curl_setopt($ch, CURLOPT_POSTFIELDS, $data_string);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    'Content-Type: application/json',
    'Content-Length: ' . strlen($data_string))
);
$result = curl_exec($ch);
//echo $result;*/
?>


