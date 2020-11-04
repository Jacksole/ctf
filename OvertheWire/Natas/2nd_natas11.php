#!/usr/bin/php7.2

<?php
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff" );

function xor_encrypt($in, $key) {

    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }
    return $outText;

}

$original = json_encode($defaultdata);

?>
