<?php

  $one++;
  $two = $one;
  $two++;
  $three = $two;
  $three++;
  $five = $three + $two;
  $ten = $five * $two;
  $handred = $ten * $ten;
  
  $H = $three * $three *  $two * $two * $two;
  $e = $handred + $one;
  $l = $handred + $two * $two * $two;
  $o = $handred + $ten + $one;
  $space = $two * $two * $two * $two * $two;
  $W = $handred - ($ten + $three);
  $r = $o + $three;
  $d = $handred;

  print chr($H);  print chr($e); print chr($l); print chr($l); print chr($o); print chr($space); print chr($W); print chr($o); print chr($r); print chr($l); print chr($d);

?>