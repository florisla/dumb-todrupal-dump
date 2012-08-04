# dumb-todrupal-dump

Small scripts to import static HTML files into a Drupal site as separate nodes.

## Concept

This combination of scripts assume you want to create Drupal nodes based on the content of a previous version of your website.

As a first step, you download a static copy of the previous website to local disk.

Next, a Python script can be run to extract the URL, title, and HTML content out of the stored HTML files.

Finally, this extracted data is imported into Drupal by a `php` file that you must place in the root of the Drupal site.

## Basic operation
1. Use `wget` to download a static copy of the websites.
2. Upload all non-HTML content files (images, CSS, ...) to the Drupal site.
3. Run `process.py` to convert HTML files into 'processed' files:

 * `articlexx.body.html`
 * `articlexx.url.txt`
 * `articlexx.title.txt`

4. Upload the processed files to the Drupal site as well, in a folder called `imports`.
5. Upload import.php to the root of the Drupal site.
6. Log in to the Drupal site as administrator and visit `/import.php`.
7. To clean up, remove `import.php` and the `imports` folder from the Drupal site.

More information can be gleaned from the scripts themselves.