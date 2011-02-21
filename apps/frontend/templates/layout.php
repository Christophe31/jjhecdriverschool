<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
    <?php include_http_metas() ?>
    <?php include_metas() ?>
    <?php include_title() ?>
    <link rel="shortcut icon" href="/favicon.ico" />
    <?php include_stylesheets() ?>
    <?php include_javascripts() ?>
  </head>
  <body>
    <div id="menu">
      <?php if($sf_user->isAuthenticated()): ?>
      hello <?php echo $sf_user->getName()?>
      <?php echo link_to('Log Out', '@sf_guard_signout'); ?>
      <?php else: ?>
      <?php echo link_to("Create Account", "sfApply/apply");?>
      <?php echo link_to('Log In', '@sf_guard_signin'); ?>
      <?php //echo $signinForm; ?>
      <?php endif ?>
        </div>    
    <?php echo $sf_content ?>

  </body>
</html>
