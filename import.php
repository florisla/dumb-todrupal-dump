<?php

// put this file in the Drupal root dir
// OR: chdir('/home/org/vitis/www/www.vitis-tct.be/');
// configure drupal root dir
define('DRUPAL_ROOT', getcwd());

// bootstrap Drupal
require_once './includes/bootstrap.inc';
drupal_bootstrap(DRUPAL_BOOTSTRAP_FULL); 

// process all files
$max_number = 104;

for ($i=0; $i<$max_number; $i++)
{
    $url = file_get_contents(sprintf("./imports/article%02d.url.txt", $i));
    $title = file_get_contents(sprintf("./imports/article%02d.title.txt", $i));
    $body = file_get_contents(sprintf("./imports/article%02d.body.html", $i));
    echo($url . "<br/>");

    // create node of the desired type
    $node = new stdClass();
    $node->type = 'page';
    node_object_prepare($node);

    // set basic data
    $node->title    = $title;
    $node->language = LANGUAGE_NONE;
    $node->uid = 3;

    // set content
    $node->body[$node->language][0]['value']   = $body;
    $node->body[$node->language][0]['summary'] = text_summary($body);
    $node->body[$node->language][0]['format']  = 'full_html'; 
    $node->path = array('alias' => $url);

    // save to database
    node_save($node);
}

?>
