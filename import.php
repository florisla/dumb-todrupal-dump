<?php

// put this file in the Drupal root dir
// OR add a line of PHP to chdir into it: chdir('/path/to/site');

// configuration:
$highest_article_number = 105;
$drupal_node_content_type = 'page';
$drupal_author_user_id = 3;

// configure drupal root dir
define('DRUPAL_ROOT', getcwd());

// bootstrap Drupal
require_once './includes/bootstrap.inc';
drupal_bootstrap(DRUPAL_BOOTSTRAP_FULL); 

// process all files
for ($i=0; $i<=$highest_article_number; $i++)
{
    // read all three files
    $url = file_get_contents(sprintf("./imports/article%05d.url.txt", $i));
    $title = file_get_contents(sprintf("./imports/article%05d.title.txt", $i));
    $body = file_get_contents(sprintf("./imports/article%05d.body.html", $i));
    echo($url . "<br/>");

    // create a new Drupal node (of the desired content type)
    $node = new stdClass();
    $node->type = $drupal_node_content_type;
    node_object_prepare($node);

    // set basic data
    $node->title    = $title;
    $node->language = LANGUAGE_NONE;
    $node->uid = $drupal_author_user_id;

    // set content
    $node->body[$node->language][0]['value']   = $body;
    $node->body[$node->language][0]['summary'] = text_summary($body);
    $node->body[$node->language][0]['format']  = 'full_html'; 
    $node->path = array('alias' => $url);

    // save to database
    node_save($node);
}

?>
